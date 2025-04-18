import keras.optimizers
import nltk
import mysql.connector
from fbchat import Client
from fbchat.models import *
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import tensorflow as tf
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD, Adam
import random

global model
words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open("reponsebot.json", encoding='utf-8').read()
intents = json.loads(data_file)

#Parcourir le fichier JSON
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Pour sortir la signifiation principale d'une phrase ou mot
        w = nltk.word_tokenize(pattern)
        words.extend(w)

        documents.append((w, intent['tag']))

        #Connecter un mot à son tag dans le fichier json
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
#Pour sortir la signifiation principale d’une phrase ou mot
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))
#Affichages
print (len(documents), "documents", documents)
#Tags
print (len(classes), "classes", classes)

print (len(words), "unique lemmatized words", words)

#Création de deux fichiers
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

# initializing training data
# Liaison pattern-lemma, pour qu'il connaisse classer les differents mots
training = []
output_empty = [0] * len(classes)
for doc in documents:

    bag = []

    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

    for w in words:
        #Ajoute a la liste bag des 1 ou des 0
        bag.append(1) if w in pattern_words else bag.append(0)


    output_row = list(output_empty)
    #Donne l'indice de la classe contenu dans doc(tuple) dans la liste classe
    output_row[classes.index(doc[1])] = 1
    # print(classes.index(doc[1]))

    training.append([bag, output_row])
# print(training)
# Pour melanger une liste
random.shuffle(training)
# print(len(training))
# print(max_length)

training = np.array(training)
# create train and test lists. X - patterns, Y -intents

train_x = list (training [:, 0])
train_y = list(training[:, 1])

# print("\a \n La taille est de ",len(train_x[0]))
# print(classes.index(documents[1]))
# print(train_y, "\a \n La taille est de ",len(train_y))
print ("Training data created")


# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax, set of training data.

model = Sequential()

model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax' ))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)

# adam=Adam(lr=0.01, decay=1e-6,ema_momentum=0.9)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])


#fitting and saving the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=250, batch_size=5, verbose=1)
# model.evaluate(np.array(train_x), np.array(train_y))
#Creer le fichier
# model.save('chatbot_model.keras', hist)

print("Model created")
'''model1=load_model('chatbot_model.h5')
print(model1)
print(model)
model1= Sequential(model1)
print(model1)'''


def save_infos(uid, username, date, heure):

    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projet_test"
    )

    curseur = connexion.cursor()

    requete = "INSERT INTO info_utilisateur (colonne1, colonne2, colonne3) VALUES (%s, %s, %s, %s)"
    donnees = (uid, username,date, heure)
    curseur.execute(requete, donnees)

    connexion.commit()

    curseur.close()
    connexion.close()


class Chatty:
    def __init__(self):
        #Models that we have created with the chatbot.py file
        self.intents = json.loads(open('reponsebot.json', encoding='utf-8').read())
        self.words = pickle.load(open('words.pkl','rb'))
        self.classes = pickle.load(open('classes.pkl','rb'))

        self.lemmatizer = WordNetLemmatizer()


    def clean_up_sentence(self, sentence):
        #Lemmantize tout les mots, pour ressortir leur signification de base
        sentence_words = nltk.word_tokenize(sentence, language="english")
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words


    def bow(self, sentence, show_details=True):
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
        print(sentence_words)
        # bag of words - matrix of N words, vocabulary matrix
        bag = [0]*len(self.words)
        for s in sentence_words:
            for i,w in enumerate(self.words):
                if w == s:
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))


    def predict_class(self,sentence):
        #Pour predire quel tag associer a la phrase
        print('We entered the PREDICT CLASS FUNCTION')
        # filter out predictions below a threshold
        p = self.bow(sentence, show_details=False)
        # print(f"p: {p}")
        # print(np.array(p))
        res = model.predict(np.array([p]))[0]
        print(f"res: {res}")
        # global ERROR_THRESHOLD
        ERROR_THRESHOLD = 0.15
        results=[]
        '''for i,r in enumerate(res):
            print("i:",i,"\t r:",r)
            if r>ERROR_THRESHOLD:
                results.append([i,r])'''
        # Cree des liste de liste avec l'indice d'un itent et sa probabilité si et seulement si la probabilité est superieure a l'erreur seuil
        results = [[i, r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        print(f"results: {results}")
        # sort by strength of probability, classe les liste de liste de la plus grande probabilité a la plus petite
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        # Liste contenant l'intent de la probabilite la plus eleve avec a valeur de celle ci
        print(f"returnlist: {return_list}")
        print('We leaving the PREDICT CLASS function')
        return return_list

    def getResponse(self, ints):
        # Apres avoir predit l'itents on cherche a obtenir une reponse, ceci en utilisant notre model
        global result
        print('We entered the GET RESPONSE FUNCTION')
        # choisi le tag avec le plus de probabilite
        tag = ints[0]['intent']
        print(f"tag: {tag}")
        list_of_intents = self.intents['intents']
        print(list_of_intents)
        # prend la probabilite de l'intent choisi et la transforme de string en reel
        proba=ints[0]['probability']
        proba= float(proba)
        if proba>0.8:
            for i in list_of_intents:
                if (i['tag'] == tag):
                    # choisit une réponse aléatoirement dans le tag choisi
                    result = random.choice(i['responses'])
                    break
        else:
            # choisit une réponse lorsque le programme ne peut repondre à une préoccupation n'a pas une reponse assez sure
            for i in list_of_intents:
                if (i['tag'] == 'noanswer'):
                    result = random.choice(i['responses'])
                    break

        print('We are leaving the GET RESPONSE FUNCTION')
        return result

    def chatbot_response(self, msg):
        print('We entered the CHATBOT RESPONSE FUNCTION')
        ints = self.predict_class(msg)
        print(f"ints: {ints}")
        res = self.getResponse(ints)
        # model.summary()
        return res

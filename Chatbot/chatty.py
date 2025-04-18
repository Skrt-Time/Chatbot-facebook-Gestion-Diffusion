import nltk
# Lemmantizer
from nltk.stem import WordNetLemmatizer
import numpy as np
import random

from keras.models import *
# from chatbot import  model
import tensorflow as tf

import pickle
import json



class Chatty:
    def __init__(self):
        # Models that we have created with the chatbot.py file
        self.intents = json.loads(open('reponsebot.json', encoding='utf-8').read())
        self.words = pickle.load(open('words.pkl', 'rb'))
        self.classes = pickle.load(open('classes.pkl', 'rb'))
        self.model = tf.saved_model.load('chatbot_model.h5')


        self.lemmatizer = WordNetLemmatizer()
    def getResponse(self, ints):
        # Apres avoir predit l'itents on cherche a obtenir une reponse, ceci en utilisant notre model
        global result
        print('We entered the GET RESPONSE FUNCTION')
        tag = ints[0]['intent']
        list_of_intents = self.intents['intents']
        for i in list_of_intents:
            if (i['tag'] == tag):
                # choisit une réponse aléatoirement
                result = random.choice(i['responses'])
                break
            else:
                result = "You must ask the right questions"
        print('We are leaving the GET RESPONSE FUNCTION')
        return result

    def chatbot_response(self, msg):
        print('We entered the CHATBOT RESPONSE FUNCTION')
        # aka = Chat()
        ints = aka.predict_class(msg)
        res = self.getResponse(ints)
        return res




'''def clean_up_sentence(self, sentence):
        #Lemmantize tout les mots, pour ressortir leur signification de base
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words


    def bow(self, sentence, show_details=True):
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
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


    def predict_class(self, sentence):
        #Pour predire quel tag associer a la phrase
        print('We entered the PREDICT CLASS FUNCTION')
        # filter out predictions below a threshold
        p = self.bow(sentence, show_details=False)
        res = self.model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        print('We leaving the PREDICT CLASS function')
        return return_list'''



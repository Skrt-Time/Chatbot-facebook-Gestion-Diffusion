import requests

def send_message(user_id, message, access_token):
    url = f"https://graph.facebook.com/v13.0/{user_id}/messages"
    params = {
        "access_token": access_token,
        "messaging_type": "UPDATE",
        "message": {
            "text": message
        }
    }
    response = requests.post(url, json=params)
    if response.status_code == 200:
        print("Message envoyé avec succès !")
    else:
        print("Échec de l'envoi du message.")

# Utilisation de la fonction send_message pour envoyer un message
user_id = '115036358326034'
message = 'Bonjour skrt!'
access_token = 'EAADJALnDRRABO3lnvwbFusqzcF4BC6aBXV4AuK5AZCrsjWu3vaYxBlnHsbrLFmiAWvZB9T8rznni3PJzmJL6S383u0SFnkVZAxh7QdhWF5H4MHpKjbZAq9EKjfnwnDBBQWZAgM29ljs1P1puC8C8raMFap5JWRTZARXcEjRIXdPd1ZAmm1kKphZBW0QwZBXhbx6uP'
send_message(user_id, message, access_token)
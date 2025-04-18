import facebook

def send_message(user_id, message, access_token):
    graph = facebook.GraphAPI(access_token)
    graph.put_object(parent_object=user_id, connection_name='messages', message=message)

# Utilisation de la fonction send_message pour envoyer un message
user_id = '115036358326034'
message = 'Bonjour skrt!'
access_token = 'EAADJALnDRRABO3lnvwbFusqzcF4BC6aBXV4AuK5AZCrsjWu3vaYxBlnHsbrLFmiAWvZB9T8rznni3PJzmJL6S383u0SFnkVZAxh7QdhWF5H4MHpKjbZAq9EKjfnwnDBBQWZAgM29ljs1P1puC8C8raMFap5JWRTZARXcEjRIXdPd1ZAmm1kKphZBW0QwZBXhbx6uP'
send_message(user_id, message, access_token)
import json
import mysql
from functions import initialize_session, send_message, set_db_connection
from colorama import Fore, Style


with open('db_config.json', 'r') as f:
    db_config = json.load(f)

# Load the API key from api_key.txt
with open('api_key.txt', 'r') as f:
    openai_api_key = f.read().strip()

db_connection = None
def initialize_db_connection(db_config):
    return mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"],
        port=db_config["port"]
    )


# function to create command line interface with user that accepts text input and sends it to gpt
def chat():
    db_connection = initialize_db_connection(db_config)
    set_db_connection(db_connection)
    messages, client = initialize_session(db_config, openai_api_key)
    while True:
        user_input = input("")
        messages.append({"role": "user", "content": user_input})
        replied_message = send_message(messages, client)
        messages.append({"role": "assistant", "content": replied_message})
        print(f"{Fore.GREEN}GPT: {replied_message}{Style.RESET_ALL}")

        if len(messages) > 10:
            pass

if __name__ == "__main__":
    chat()
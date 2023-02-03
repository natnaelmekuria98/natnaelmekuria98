# important library must be install 
import openai   
import requests
import json

# Initialize the OpenAI API key
openai.api_key = "your_openai.api_key"   # opeAI API secret key

# Define a function to generate the response from ChatGPT
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Define a function to handle the incoming messages from Telegram
def handle_message(message):
    response = generate_response(message)
    return response

# Define a function to send a message to Telegram
def send_message(chat_id, message):
    #url = f"https://api.telegram.org/bot<your_telegram_bot_token>/sendMessage?chat_id={chat_id}&text={message}"  #telegram bot token
    url = f"https://api.telegram.org/bot<your_telegram_bot-token>/sendMessage?chat_id={chat_id}&text={message}"  #telegram bot token
    requests.get(url)

# Define the main function to run the Telegram Bot
def lambda_handler(event, context):
    body = json.loads(event["body"])
    message = body["message"]["text"]
    chat_id = body["message"]["chat"]["id"]

    response = handle_message(message)
    send_message(chat_id, response)

    return {
        "statusCode": 200,
        "body": json.dumps({}),
    }



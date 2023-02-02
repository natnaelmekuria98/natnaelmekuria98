
#LIBRARY dependance 
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

## openAI CREDENTIALS 
openai.api_key = "your OpenAI KEY"

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    # Get the message sent from the user
    msg = request.values.get("Body", None)

    # Use OpenAI's GPT-3 to generate a response to the incoming message
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Your message: " + msg + "\n\nRespond:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Create a Twilio response object to be able to send a reply back
    resp = MessagingResponse()

    # Add the response from OpenAI's GPT-3 to the Twilio response
    resp.message(response)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

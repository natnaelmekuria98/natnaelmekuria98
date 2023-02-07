#Import some important library
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# set up the OpenAI API key
openai.api_key = " "  #here you have to use your own openAI API key

# set up the Telegram bot
bot = telegram.Bot(token='6007228593:AAESmIC9Ym3lFAd9Awu0AlU7WwrJXg-idms')    #here you have to use your own telegram token
updater = Updater(token='6007228593:AAESmIC9Ym3lFAd9Awu0AlU7WwrJXg-idms', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Wellcome To ChatGPT Telegram Chatbot.You can ask me any questions you want and i am ready to answer")

def echo(update, context):
    user_input = update.message.text
    response = openai.Completion.create(engine="text-davinci-002", prompt=f"{user_input}")
    response = response.choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

start_handler = CommandHandler("start", start)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()



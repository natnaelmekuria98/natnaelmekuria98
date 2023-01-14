import tkinter as tk
from tkinter import ttk
import openai

# Authenticate to the OpenAI API

openai.api_key = "Your-openAI-KEY"



def chatbot_response(user_input):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{user_input}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,


    )
    return response['choices'][0]['text']

def send():
    # Get the user's input and display it in the chat history
    user_input = user_entry.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

    # Get the chatbot's response and display it in the chat history
    bot_response = chatbot_response(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "AI Chatbot: " + bot_response + "\n")
    chat_history.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("ChatGPT Chatbot With Custom GUI")

# Create the widgets
user_entry = ttk.Entry(root, width=50)
send_button = ttk.Button(root, text="Send Message", command=send)
chat_history = tk.Text(root, width=50, height=20, wrap=tk.WORD, state=tk.DISABLED)

# Add the widgets to the window
user_entry.pack()
send_button.pack()
chat_history.pack()

# Start the main loop
root.mainloop()


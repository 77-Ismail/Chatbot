import tkinter as tk
import re
import main

# Create a Tkinter window
window = tk.Tk()
window.title("ChatBot")

# Create a Text widget to display the conversation
conversation_text = tk.Text(window, height=20, width=50)
conversation_text.pack()

# Function to handle user input and display the response
def handle_input():
    user_input = input_entry.get()
    response = main.get_response(user_input)

    conversation_text.insert(tk.END, "You: " + user_input + "\n")
    conversation_text.insert(tk.END, "Bot: " + response + "\n")
    input_entry.delete(0, tk.END)

# Create an Entry widget for user input
input_entry = tk.Entry(window, width=50)
input_entry.pack()

# Create a button to handle user input
send_button = tk.Button(window, text="Send", command=handle_input)
send_button.pack()

# Start the Tkinter event loop
window.mainloop()

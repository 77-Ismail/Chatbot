import tkinter as tk
import re
import long_responses as long


# Function to handle user input and display the response
def handle_input():
    user_input = input_entry.get()
    response = get_response(user_input)

    print('Bot:', response)
    conversation_text.insert(tk.END, "You: " + user_input + "\n")
    conversation_text.insert(tk.END, "Bot: " + response + "\n")
    input_entry.delete(0, tk.END)  #Input Entry is basically field

# Create a Tkinter window
window = tk.Tk()
window.geometry("730x550")
window.title("ChatBot-PYTHON-CLASS-01")

# Create a Text widget to display the conversation
conversation_text = tk.Text(window, height=30, width=60)
conversation_text.pack()  #Pack is used to add these in window

# Create an Entry widget for user input
input_entry = tk.Entry(window, bg="beige",width=50)
input_entry.pack()

# Create a button to handle user input
send_button = tk.Button(window, text="Send",bg="crimson",fg="white" ,command=handle_input,width=20,padx=5)
send_button.pack()

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Your existing chatbot logic code
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}  # Empty Dictionary

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response
    response('Yes, what can i do for you!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('what happened could you please brief me?', ['oh'], required_words=['oh'])

    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Happy to hear this Sir, Anything else', ['i', 'am', 'good'], required_words=['am', 'good'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('That\'s Nice!', ['i', 'love', 'to', 'code'], required_words=['love', 'code'])


    #Dr Amir

    #Adding Multiple Responses For chatbot Related to Agriculture---------------------------------------------------
    response(long.R_AGRICULTURE, ['define', 'agriculture'], single_response=True)
    response(long.R_AGRICULTURE, ['what', 'is', 'agriculture'], required_words=['what', 'agriculture'])

    #Question 1
    response(long.R_QUESTION_1, ['How', 'can', 'I', 'improve', 'the', 'fertility', 'of', 'my', 'soil'], required_words=['improve', 'fertility', 'soil'])

    # Question 2
    response(long.R_QUESTION_2, ['What', 'are', 'some', 'natural', 'methods', 'to', 'control', 'pests', 'in', 'my','garden'], required_words=['natural', 'methods', 'pests', 'control', 'garden'])

    # Question 3
    response(long.R_QUESTION_3, ['How', 'do', 'I', 'determine', 'the', 'right', 'amount', 'of', 'water', 'to', 'give', 'my', 'plants'], required_words=['right', 'amount', 'water'])

    # Question 4
    response(long.R_QUESTION_4, ['What', 'are', 'the', 'best', 'crops', 'to', 'grow', 'in', 'my', 'specific', 'climate'], required_words=['best', 'crops'])

    # Question 5
    response(long.R_QUESTION_5, ['How', 'do', 'I', 'prevent', 'weeds', 'from', 'overtaking', 'my', 'garden'], required_words=['prevent', 'weeds', 'garden'])

    # Question 6
    response(long.R_QUESTION_6, ['What', 'is', 'organic', 'farming', 'and', 'how', 'can', 'I', 'incorporate', 'it', 'into', 'my', 'practices'], required_words=['organic', 'farming', 'practices'])

    # Question 7
    response(long.R_QUESTION_7, ['How', 'can', 'I', 'protect', 'my', 'crops', 'from', 'diseases'], required_words=['protect', 'diseases'])

    # Question 8
    response(long.R_QUESTION_8, ['What', 'are', 'some', 'effective', 'ways', 'to', 'increase', 'crop', 'yield'], required_words=['increase', 'crop'])

    # Question 9
    response(long.R_QUESTION_9, ['How', 'do', 'I', 'compost', 'organic', 'waste', 'to', 'create', 'nutrient', 'rich', 'soil'], required_words=['compost', 'organic','nutrient','rich','soil'])

    # Question 10
    response(long.R_QUESTION_10, ['What', 'are', 'the', 'benefits', 'of', 'crop', 'rotation', 'and', 'how', 'can', 'I', 'implement', 'it'], required_words=['what', 'agriculture'])

    # Question 11
    response(long.R_QUESTION_11, ['How', 'do', 'I', 'select', 'the', 'right', 'seeds', 'for', 'my', 'agricultural', 'needs'], required_words=['seeds', 'agricultural','agriculture'])

    # Question 12
    response(long.R_QUESTION_12, ['What', 'are', 'some', 'sustainable', 'irrigation', 'techniques'], required_words=['sustainable', 'irrigation'])

    # Question 13
    response(long.R_QUESTION_13, ['How', 'can', 'I', 'prevent', 'soil', 'erosion', 'on', 'my', 'farm'], required_words=['prevent', 'soil', 'erosion'])

    # Question 14
    response(long.R_QUESTION_14, ['What', 'are', 'the', 'best', 'practices', 'for', 'greenhouse', 'gardening'], required_words=['greenhouse', 'gardening'])

    # Question 15
    response(long.R_QUESTION_15, ['How', 'do', 'I', 'maintain', 'proper', 'nutrient', 'balance', 'in', 'my', 'hydroponic', 'system?'], required_words=['nutrient', 'balance'])

    # Question 16
    response(long.R_QUESTION_16, ['What', 'are', 'the', 'advantages', 'of', 'using', 'cover', 'crops', 'in', 'farming'], required_words=['advantages', 'cover','crops'])

    # Question 17
    response(long.R_QUESTION_17, ['How', 'can', 'I', 'increase', 'the', 'efficiency', 'of', 'my', 'farm', 'equipment'], required_words=['increase', 'efficiency'])

    # Question 18
    response(long.R_QUESTION_18, ['How', 'do', 'I', 'identify', 'and', 'treat', 'nutrient', 'deficiencies', 'in', 'plants'], required_words=['what', 'agriculture'])

    # Question 19
    response(long.R_QUESTION_19, ['What', 'are', 'the', 'potential', 'risks', 'and', 'benefits', 'of', 'genetically', 'modified', 'organisms', '(GMOs)', 'in', 'agriculture'], required_words=['what', 'agriculture'])

    # Question 20
    response(long.R_QUESTION_20, ['How', 'can', 'I', 'start', 'a', 'small','scale', 'urban', 'garden'], required_words=['small', 'scale'])

    #----------------------------------------------------------------------------------------------------------------

    # Longer responses
    response(long.R_JOKE, ['Tell', 'me', 'something', 'funny'], required_words=['something', 'funny'])
    response(long.R_PYTHON_ROADMAP, ['Suggest', 'python', 'roadmap'], required_words=['python', 'roadmap'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match  # This will check the response probability has less then 1 like not any best match in this then check in long response for this.

# Start the Tkinter event loop

window.mainloop()

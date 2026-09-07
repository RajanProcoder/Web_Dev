import datetime

# Get the current hour (0 to 23)
current_hour = datetime.datetime.now().hour

name = input("Enter Your Name: ")

# Logical conditions based on 24-hour clock
if 5 <= current_hour < 12:
    print("Good Morning,", name)
elif 12 <= current_hour < 17:
    print("Good Afternoon,", name)
elif 17 <= current_hour < 21:
    print("Good Evening,", name)
else:
    print("Good Night,", name)

print("____"*15)
print("Swagat hai, i am smart AI Assistent ChatBot")
print("Ask Me Some basic Question, (Bye or Q )")
print("____"*15)

questions_dict = {
    # --- Basic Greetings / सामान्य बातचीत (1-15) ---
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I am doing great, thank you! How are you?",
    "good morning": "Good morning! Have a wonderful day ahead.",
    "good afternoon": "Good afternoon! How is your day going?",
    "good evening": "Good evening! Hope you are having a relaxed time.",
    "good night": "Good night! Sweet dreams.",
    "who are you": "I am a smart chatbot assistant created to help you.",
    "what is your name": "You can call me Smart Chatbot.",
    "who made you": "I was created by a smart developer using Python.",
    "are you human": "No, I am an AI assistant, but I love chatting with humans!",
    "what can you do": "I can answer your questions, chat with you, and help you learn.",
    "thank you": "You're very welcome! Happy to help.",
    "thanks": "Anytime! Let me know if you need anything else.",
    "bye": "Goodbye! Have a great day ahead.",

    # --- India GK / भारत का सामान्य ज्ञान (16-45) ---
    "india capital": "The capital of India is New Delhi.",
    "capital of india": "New Delhi is the capital of India.",
    "national bird of india": "The national bird of India is the Peacock.",
    "national animal of india": "The national animal of India is the Bengal Tiger.",
    "national flower of india": "The national flower of India is the Lotus.",
    "national fruit of india": "The national fruit of India is the Mango.",
    "national anthem of india": "The national anthem of India is 'Jana Gana Mana'.",
    "national song of india": "The national song of India is 'Vande Mataram'.",
    "who is prime minister of india": "The Prime Minister of India is Narendra Modi.",
    "who is president of india": "The President of India is Droupadi Murmu.",
    "financial capital of india": "Mumbai is known as the financial capital of India.",
    "pink city of india": "Jaipur is known as the Pink City of India.",
    "silicon valley of india": "Bengaluru is known as the Silicon Valley of India.",
    "highest mountain in india": "Kanchenjunga is the highest mountain peak located in India.",
    "longest river in india": "The Ganges (Ganga) is the longest river in India.",
    "largest state in india": "Rajasthan is the largest state in India by area.",
    "smallest state in india": "Goa is the smallest state in India by area.",
    "most populated state in india": "Uttar Pradesh is the most populated state in India.",
    "least populated state in india": "Sikkim is the least populated state in India.",
    "currency of india": "The currency of India is the Indian Rupee (INR).",
    "independence day of india": "India celebrates its Independence Day on 15th August.",
    "republic day of india": "India celebrates its Republic Day on 26th January.",
    "national game of india": "Field Hockey is widely considered the national sport of India.",
    "taj mahal location": "The Taj Mahal is located in Agra, Uttar Pradesh.",
    "gateway of india location": "The Gateway of India is located in Mumbai.",
    "india gate location": "The India Gate is located in New Delhi.",
    "isro full form": "ISRO stands for Indian Space Research Organisation.",
    "first president of india": "Dr. Rajendra Prasad was the first President of India.",
    "first prime minister of india": "Pandit Jawaharlal Nehru was the first Prime Minister of India.",
    "how many states in india": "There are 28 states and 8 Union Territories in India.",

    # --- Common Technical / Python Questions (46-75) ---
    "what is python": "Python is a high-level, interpreted, and easy-to-learn programming language.",
    "who created python": "Python was created by Guido van Rossum and released in 1991.",
    "is python free": "Yes, Python is an open-source and completely free language.",
    "what is a variable": "A variable is a container or name used to store data values in memory.",
    "what is a list": "A list is an ordered, mutable collection of items written inside square brackets [].",
    "what is a tuple": "A tuple is an ordered, immutable collection of items written inside parentheses ().",
    "what is a dictionary": "A dictionary is an unordered collection of data stored in key-value pairs inside {}.",
    "what is a string": "A string is a sequence of characters enclosed in single or double quotes.",
    "what is an integer": "An integer is a whole number, positive or negative, without decimals.",
    "what is a float": "A float is a number that contains decimal points.",
    "what is boolean": "A boolean represents one of two values: True or False.",
    "how to print in python": "You use the print() function to display output on the screen.",
    "how to take input in python": "You use the input() function to take user input from the keyboard.",
    "what is indentation": "Indentation is the whitespaces at the start of a code line used to define code blocks.",
    "what is a comment": "A comment is non-executable text used for explanations, written with a '#' symbol.",
    "what is a function": "A function is a reusable block of code that runs only when it is called.",
    "how to define function": "You define a function using the 'def' keyword followed by the function name.",
    "what is a loop": "A loop is used to repeat a block of code multiple times until a condition is met.",
    "types of loops": "Python mainly has two types of loops: 'for' loop and 'while' loop.",
    "what is pip": "PIP is the standard package manager used to install additional Python modules.",
    "what is a module": "A module is a file containing Python code (functions, classes) that you can import.",
    "what is a class": "A class is a blueprint or template for creating objects in Object-Oriented Programming.",
    "what is an object": "An object is an instance of a class that holds actual data and functions.",
    "what is oops": "OOPs stands for Object-Oriented Programming, based on classes and objects.",
    "what is lambda": "A lambda function is a small, anonymous, single-line function in Python.",
    "what is len function": "The len() function returns the number of items or characters in an object.",
    "what is range function": "The range() function returns a sequence of numbers, starting from 0 by default.",
    "what is local variable": "A variable declared inside a function that can only be used within that function.",
    "what is global variable": "A variable declared outside any function that can be accessed anywhere in the code.",
    "what is an error": "An error or exception is a mistake in code that stops the program from running.",

    # --- General Knowledge & Fun / सामान्य ज्ञान और मज़ाक (76-100) ---
    "capital of usa": "The capital of the United States is Washington, D.C.",
    "largest ocean": "The Pacific Ocean is the largest ocean on Earth.",
    "fastest animal": "The Cheetah is the fastest land animal on Earth.",
    "tallest animal": "The Giraffe is the tallest living land animal.",
    "how many days in a year": "There are 365 days in a normal year and 366 days in a leap year.",
    "how many hours in a day": "There are 24 hours in a single day.",
    "how many continents": "There are 7 continents on Earth.",
    "largest continent": "Asia is the largest continent in the world by both area and population.",
    "smallest continent": "Australia is the smallest continent in the world.",
    "brightest star": "Sirius (also known as the Dog Star) is the brightest star in the night sky.",
    "closest planet to sun": "Mercury is the closest planet to the Sun.",
    "largest planet": "Jupiter is the largest planet in our solar system.",
    "red planet": "Mars is commonly known as the Red Planet.",
    "hottest planet": "Venus is the hottest planet in our solar system.",
    "who discovered gravity": "Sir Isaac Newton is famous for discovering the law of gravity.",
    "who invented light bulb": "Thomas Edison is credited with inventing the practical electric light bulb.",
    "what is water formula": "The chemical formula for water is H2O.",
    "what is brain of computer": "The CPU (Central Processing Unit) is known as the brain of the computer.",
    "what is www": "WWW stands for World Wide Web.",
    "what is html": "HTML stands for HyperText Markup Language, used to create web pages.",
    "are you smart": "I try my best! I am always learning new things.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "do you love python": "Yes! Python is my foundation. I think it is the best language.",
    "make me laugh": "What do you call a computer that sings? A Dell!",
    "good job": "Thank you! I am happy to help anytime."
}

# --- Chat Loop Logic (चैट लूप लॉजिक) ---
while True:
    # यूज़र से इनपुट लेना, उसे छोटे अक्षरों (lowercase) में बदलना और एक्स्ट्रा स्पेस हटाना
    user_input = input("\nYou: ").lower().strip()
    
    # बाहर निकलने की कंडीशन (Quit condition)
    if user_input == 'q' or user_input == 'bye':
        print("Bot: Goodbye! Have a great day ahead.")
        break
        
    # खाली इनपुट चेक करना
    if user_input == "":
        continue
        
    # डिक्शनरी में सवाल ढूंढना
    if user_input in questions_dict:
        print(f"Bot: {questions_dict[user_input]}")
    else:
        print("Bot: Sorry, accurate answer nahi mila. Please try another question!")

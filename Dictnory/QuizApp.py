# # Quiz Questions & Answers




python_basic_qa = {
    "What is the symbol used to define a list?": "[]",
    "How do you represent a positive number sign in Python?": "+",
    "How do you represent a negative number sign in Python?": "-",
    "What function is used to print output to the screen?": "print()",
    "Which function is used to take input from the user?": "input()",
    "What data type is used for whole numbers?": "int",
    "What data type is used for decimal numbers?": "float",
    "What data type represents text?": "str",
    "What are the two values of a Boolean data type?": "True and False",
    "Which symbol is used for single-line comments?": "#",
    "Which operator is used for addition?": "+",
    "Which operator is used for subtraction?": "-",
    "Which operator is used for multiplication?": "*",
    "Which operator is used for standard division?": "/",
    "Which operator is used for floor division (integer result)?": "//",
    "Which operator gives the remainder of a division (modulus)?": "%",
    "Which operator is used for exponents (power)?": "**",
    "Which symbol is used to assign a value to a variable?": "=",
    "Which operator checks if two values are equal?": "==",
    "Which operator checks if two values are not equal?": "!=",
    "Is Python case-sensitive?": "Yes",
    "What keyword is used to start an 'if' statement?": "if",
    "What keyword is used for an alternative condition if 'if' fails?": "elif",
    "What keyword handles all cases if conditions are not met?": "else",
    "What symbol is used to start a code block after an if/loop?": ":",
    "What loop is used when you know the number of iterations?": "for",
    "What loop runs as long as a condition is true?": "while",
    "What keyword is used to exit a loop prematurely?": "break",
    "What keyword skips the current iteration of a loop?": "continue",
    "What function generates a sequence of numbers?": "range()",
    "What keyword is used to define a function?": "def",
    "What keyword is used to send a value back from a function?": "return",
    "What symbol is used to define a dictionary?": "{ }",
    "What symbol is used to define a tuple?": "( )",
    "Are lists mutable (changeable)?": "Yes",
    "Are tuples mutable?": "No",
    "What method adds an element to the end of a list?": "append()",
    "What method removes all items from a list?": "clear()",
    "What function returns the length of an object?": "len()",
    "What method converts a string to lowercase?": "lower()",
    "What method converts a string to uppercase?": "upper()",
    "Which operator checks if a value exists inside a sequence?": "in",
    "What is the index of the first element in a list?": "0",
    "What index represents the last element in a list?": "-1",
    "What function converts a value into a string?": "str()",
    "What function converts a value into an integer?": "int()",
    "What error occurs when you mismatch indentation?": "IndentationError",
    "What block is used to catch and handle errors?": "try except",
    "What keyword is used to import a module?": "import",
    "What is the core philosophy of Python called?": "The Zen of Python"
}

score = 0
Count = 1

for question, Correct_anser in python_basic_qa.items():
    ans_wer = input(f"\n{Count}. Question -> {question}\n[Answer likho]: ")
    Count += 1

    #  Fix: Dono taraf .strip().lower() kar diya
    if ans_wer.strip().lower() == Correct_anser.strip().lower():
        print("✅ Right Answer Brother!")
        score += 1
    else:
        score -= 1
        print(f"❌ Wrong Answer || Right Answer is: {Correct_anser}")

print("\n--------------------------------")
print(f"🎯 Total Score is = {score} / {len(python_basic_qa)}")















#=======================================================================
# quiz = {
#     "Python me Dictionary kis symbol se banti hai?": "{}",
#     "Python me List kis symbol se banti hai?": "[]",
#     "Capital of India?": "Delhi"
# }

# score = 0

# print("=== Python Mini Quiz ===")

# # Dict items par loop
# for question, correct_answer in quiz.items():
#     user_ans = input(f"\nQuestion: {question}\nYour Answer: ")
    
#     # Case insensitive comparison (.strip() & .lower())
#     if user_ans.strip().lower() == correct_answer.lower():
#         print("✅ Sahi Jawab!")
#         score += 1
#     else:
#         print(f"❌ Galat! Sahi answer tha: {correct_answer}")

# print("\n--- Final Result ---")
# print(f"Aapka Score: {score} / {len(quiz)}")





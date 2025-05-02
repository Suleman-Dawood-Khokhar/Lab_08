#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical formula for salt?", "NaCl"),
        ("Who developed the theory of relativity?", "Albert Einstein"),
        ("What is the process by which plants make their own food?", "Photosynthesis"),
        ("What gas do plants absorb during photosynthesis?", "Carbon dioxide"),
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which country has the most natural lakes?", "Canada"),
        ("What is the largest desert in the world?", "Sahara Desert"),
        ("Which river is the longest in the world?", "Nile River"),
        ("Which continent is the Sahara Desert located on?", "Africa"),
    ],
    "History": [
        ("Who was the first president of the United States?", "George Washington"),
        ("What year did World War II end?", "1945"),
        ("Which empire was ruled by Julius Caesar?", "Roman Empire"),
        ("In what year did the Titanic sink?", "1912"),
        ("Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart"),
    ],
    "Literature": [
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
        ("What is the title of the first Harry Potter book?", "Harry Potter and the Sorcerer's Stone"),
        ("Who wrote '1984'?", "George Orwell"),
        ("What novel begins with 'Call me Ishmael'?", "Moby-Dick"),
        ("Who wrote 'Pride and Prejudice'?", "Jane Austen"),
    ],
    "Sports": [
        ("Which country hosted the 2016 Summer Olympics?", "Brazil"),
        ("Who won the FIFA World Cup in 2018?", "France"),
        ("How many players are there in a basketball team?", "5"),
        ("Which sport is known as 'the beautiful game'?", "Soccer"),
        ("Who holds the record for the most Olympic gold medals?", "Michael Phelps"),
    ]
}


hints = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical formula for salt?", "NaCl"),
        ("Who developed the theory of relativity?", "Albert Einstein"),
        ("What is the process by which plants make their own food?", "Photosynthesis"),
        ("What gas do plants absorb during photosynthesis?", "Carbon dioxide"),
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which country has the most natural lakes?", "Canada"),
        ("What is the largest desert in the world?", "Sahara Desert"),
        ("Which river is the longest in the world?", "Nile River"),
        ("Which continent is the Sahara Desert located on?", "Africa"),
    ],
    "History": [
        ("Who was the first president of the United States?", "George Washington"),
        ("What year did World War II end?", "1945"),
        ("Which empire was ruled by Julius Caesar?", "Roman Empire"),
        ("In what year did the Titanic sink?", "1912"),
        ("Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart"),
    ],
    "Literature": [
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
        ("What is the title of the first Harry Potter book?", "Harry Potter and the Sorcerer's Stone"),
        ("Who wrote '1984'?", "George Orwell"),
        ("What novel begins with 'Call me Ishmael'?", "Moby-Dick"),
        ("Who wrote 'Pride and Prejudice'?", "Jane Austen"),
    ],
    "Sports": [
        ("Which country hosted the 2016 Summer Olympics?", "Brazil"),
        ("Who won the FIFA World Cup in 2018?", "France"),
        ("How many players are there in a basketball team?", "5"),
        ("Which sport is known as 'the beautiful game'?", "Soccer"),
        ("Who holds the record for the most Olympic gold medals?", "Michael Phelps"),
    ]
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    if category in questions:
        rand = random.randint(0,len(questions[category]-1))
    return questions[category][rand]
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    return player_answer==correct_answer
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    lis =  questions[category]
    for i in lis:
        if i[0]== question:
            lis.remove(i)
            questions[category] = lis
            break
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------

    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------
    print(question)
    ans = str(input("Enter the anwer  :"))
    return ans 
    
#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    lis =  hints[category]
    for i in lis:
        if i[0]== question:
            return i[1]
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"Correct answer : {correct_answer}")
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------





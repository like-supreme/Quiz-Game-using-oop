"""
main notes

In the data part, there is a list of dictionaries.
What we want to create is a list of question objects.
We have already created a class named Question.
Task: Write a for loop to iterate over the question_data.
Create a Question object from each entry in question_data.
Append each Question object to the question_bank.
"""
#===========================================================
"""
question model notes
We will create a question module.
Create a Question class with an __init__ method that has two attributes: text and answer.



import random
from data import question_data as data_list
       
class Question:
    def __init__(self):
        question = random.choice(data_list)
        self.text = question["text"]
        self.answer = question["answer"] # I really forgot how to use it. I used .keys and .values as if it was a list.
"""
"""
quizbrain notes
TODO: asking the questions
TODO: checking if the answer was correct
TODO: checking if we're at the end of the quiz
Attributes: question_number = 0
questions_list
Method: next_question()

Create a class called QuizBrain
Write an __init__ method
Initialize the question_number to 0
Initialize the question_list using an input parameter

Write a method called next_question. This method should get the current item from the question list
using the current question number, then show the question text using input().

Next step:
Create a method called still_has_questions +
Return a boolean depending on the value of question_number
Use a while loop to show the next question
Think about how the question number and the length of the question list are related
and complete this part.
We will also add score as an attribute.
Add check_answer as a method.
"""

"""
From https://opentdb.com/ you can choose your own questions and get them as an API.
Then you can bring the dataset and paste it into the question part.
The only thing you need to change is the text and answer part in the main file.
There is no need to change the data of the classes or any other values.
This is one of the best examples of how effective object-oriented programming is.
"""

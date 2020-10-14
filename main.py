import random
import string
import inquirer
from inquirer.themes import GreenPassion


questions = [
    inquirer.List('choices',
                message="Options?",
                choices=['week', 'good', 'strong', 'exit'],
            ),
]

length = [
    inquirer.List('length', 
        message="Your password length: ",
        choices=["8" ,  "12" , "14" , "18"],
    )
]

while True:
    answers = inquirer.prompt(questions, theme=GreenPassion())



    if answers['choices'] == "week":
        weekLetters = string.ascii_letters
        passLength = inquirer.prompt(length)
        generatedPass = ''.join(random.choice(weekLetters) for i in range(int(passLength['length'])))
        print(generatedPass)

    elif answers['choices'] == "good":
        goodLetters = ''.join(string.ascii_letters) + ''.join(string.digits)
        passLength = inquirer.prompt(length)
        generatedPass = ''.join(random.choice(goodLetters) for i in range(int(passLength['length'])))
        print(generatedPass)

    elif answers['choices'] == "strong":
        strongLetters = string.printable
        # strongLetters = strongLetters.replace[" ", ""]
        # strongLetters = strongLetters.replace["\n", ""]
        passLength = inquirer.prompt(length)
        generatedPass = ''.join(random.choice(strongLetters) for i in range(int(passLength['length'])))
        print(generatedPass)

    elif answers['choices'] == "exit":
        break



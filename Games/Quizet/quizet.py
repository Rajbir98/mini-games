import requests
import html
import re
import os
import time
from random import shuffle
from random import randint
from random import choice
import json

# You're public now

user = os.path.expanduser("~/Quizet/")
if not os.path.exists(user):
  os.makedirs(user)
os.chmod(user, 0o777)

title = """
                          ___        _         _   _
                         / _ \ _   _(_)_______| |_| |
                        | | | | | | | |_  / _ \ __| |
                        | |_| | |_| | |/ /  __/ |_|_|
                         \__\_\\__,_|_/___\___|\__(_)
        """ + "\n\n"


def display_menu():
  print(title)
  print("             1. Start Quiz\n")
  # print("             2. Options\n")
  print("             2. Exit\n")


def main():
  while True:
    display_menu()
    choice = input("             ")
    if choice == "1":
      game()
    # elif choice == "2":
    #     option()
    elif choice == "2":
      exit()
    else:
      print("             Invalid choice. Try again.")
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')


def progress_bar(current, total):
  per = (current / total) * 100
  filled = int(25 * current / total)
  bar = '=' * filled + '-' * (25 - filled)
  print(f'\n\r             [{bar}] {per}%\n', end="")


def game():
  os.system('cls' if os.name == 'nt' else 'clear')
  time.sleep(1)
  print(title)
  print("             Quiz Parameters\n")
  amt = int(
    input(
      "              How many questions do you want to attempt?\n\n               "
    ))
  dif = str(
    input(
      "\n              What should be the difficulty?(easy, medium, hard)\n\n               "
    )).lower()
  os.system('cls' if os.name == 'nt' else 'clear')
  print(title)
  try:
    if os.path.exists(user + f"questions_{amt}_{dif}.json"):
      with open(user + f"questions_{amt}_{dif}.json", "r") as file:
        questions = json.load(file)
      if randint(0, 5) == 1:
        os.remove(user + f"questions_{amt}_{dif}.json")
    else:
      response = requests.get(
        f'https://opentdb.com/api.php?amount={amt}&difficulty={dif}&type=multiple'
      )
      questions = response.json()
      with open(user + f"questions_{amt}_{dif}.json", "w") as file:
        json.dump(questions, file)
  except Exception as e:
    print(e)
    print("             Internet connection is not available\n")
    resp = str(
      input("             Do want to continue to offline mode (y/n) : "))
    if resp.lower() == 'n':
      exit()
    else:
      json_files = [f for f in os.listdir(user) if f.endswith('.json')]
      if os.path.exists(user + f"questions_{amt}_{dif}.json"):
        with open(user + f"questions_{amt}_{dif}.json", "r") as file:
          questions = json.load(file)
      elif json_files:
        print("             Question not found.\n")
        time.sleep(1)
        print("             Loading a random question...")
        random_file = choice(json_files)
        with open(random_file, "r") as file:
          questions = json.load(file)
      else:
        print("             No offline questions found.")
        time.sleep(5)
        exit()

  question_list = []
  for i in questions['results']:
    options = [
      html.unescape(re.sub(r'[^\x00-\x7F]+', '', option))
      for option in i['incorrect_answers']
    ]
    options.insert(
      1, html.unescape(re.sub(r'[^\x00-\x7F]+', '', i['correct_answer'])))
    shuffle(options)
    question_dict = {
      'question': html.unescape(re.sub(r'[^\x00-\x7F]+', '', i['question'])),
      'options': options,
      'answer': i['correct_answer']
    }
    question_list.append(question_dict)
    shuffle(question_list)

  os.system('cls' if os.name == 'nt' else 'clear')
  score = 0

  for i in range(0, len(question_list)):
    print(title)
    progress_bar(i, amt)
    print('\n\n')
    print('  ' + question_list[i]['question'] + '\n')
    for idx, opt in enumerate(question_list[i]['options']):
      print(f"    {idx+1}. {opt}")
    # print(question_list[i]['answer'])
    print('\n')
    resp = int(input("    .) "))
    if question_list[i]['options'][resp - 1] == question_list[i]['answer']:
      score += 1
      print(
        f"  Correct Answer!\n  Your Score is {score*10}")
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')

    else:
      print(
        f"  Sadly Your Answer is Wrong!, The Answer was {question_list[i]['answer']}\n  Your Highest Score was {score*10}"
      )
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')
      break

  print(title)
  print(f"             Your Score was {score*10}")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')


main()

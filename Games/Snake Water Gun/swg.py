'''
Main Idea...

We know that in Snake, Water, Gun

We have, 

  if Snake V/S Water [Snake Wins]
  if Water V/S Gun   [Water Wins]
  if Snake V/S Gun   [Gun   Wins]
  
Let’s associate each possibility with a number:

  1: Snake
  2: Water
  3: Gun

If we combine those numbers and the rules of the game, we get:
  Here, '>' indicates towards the winner,

    1 > 2 *
    2 > 3 *
    3 > 1 **

So, we got a pattern here,

    If both numbers are the same, no one wins
    If both numbers are consecutive, the smaller one wins (*)
    If both numbers aren’t consecutive, the bigger one wins (**)

Thanks for reading...
'''

# Importing Modules

from random import choice  # For choosing random option
from enum import Enum  # To denote options with integers
from os import system  # To clear the terminal
from os import environ as env  # Fun Username Call

proceed = True  # Loop Check
username = env["REPL_OWNER"]  # The Cool One

while proceed:  # Game Loop

  print("THE SNAKE WATER GUN GAME\n")  # Fun Title

  print("Welcome {}!\n".format(username))

  # Taking Input

  P = choice(['snake', 'water', 'gun'])
  p = str(input("Your Choice: ")).lower()

  # Converting Inputs to be more user-friendly

  if p in ['s', '1']:
    p = 'snake'
  elif p in ['w', '2']:
    p = 'water'
  elif p in ['g', '3']:
    p = 'gun'

  # List of spicy text
  words = ["Drank The Water", "Spilled Over The Gun", "Shot The Snake"]

  # Clearing the Terminal (not necessary)
  system('clear')

  # Setting up Enum


  class opt(Enum):
    snake = 1
    water = 2
    gun = 3

  # Getting the results

  choices = [opt[p].value, opt[P].value]  # Stores the Choices

  result = choices[1] - choices[0]  # Returns 0 or 1 or -1

  # Showing Inputs

  print(f'\n\nThe Player Chose {p.title()}')
  print(f'The Opponent Chose {P.title()}\n\n')

  # Annoucing Results

  if result == 0:  # Reffer Line Number 75
    print("A Passive Match\n\nIt's a Draw")

  elif result in [1, -1]:  # Reffer Line Number 75
    print(f'The {opt(min(choices)).name.title()} {words[min(choices)-1]}')
    if p == opt(min(choices)).name:
      print("\nYou won the Game!")
    else:
      print("\nYou lost the Game!")

  else:
    print(f'The {opt(max(choices)).name.title()} {words[max(choices)-1]}')
    if p == opt(max(choices)).name:
      print("\nYou won the Game!")
    else:
      print("\nYou lost the Game!")

  if input("Play Again? (y/n): ").lower() == 'y':  # Continue?
    proceed = True
    # Clearing the Terminal (pretty necessary)
    system('clear')
  else:
    proceed = False

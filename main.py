import random
from game_data import data
from replit import clear
from art import logo 
from art import vs



def format_data(account):
  """Prints the account data"""

  account_descr = account["description"]
  account_name = account["name"]
  account_country = account["country"]

  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """checks which account has the highest follower count. """

  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    

score = 0
account_b = random.choice(data)

is_game_over = False
while not is_game_over:

  account_a = account_b  
  while account_b == account_a:
    account_b = random.choice(data)

  print(logo)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")
  
  guess = input("Who do you think has higher follower count on Instagram. A or B? ").lower()
  

  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]

  is_correct = check_answer(guess, a_followers, b_followers) 
  
  clear()
  if is_correct:
    score += 1
    print(f"You are right! Current score: {score}")  

  else:
    print("Oops, Wrong answer!")
    is_game_over = True

print(f"Your score is {score}.")

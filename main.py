import random

Run = True


def greeting():
  name = input("What is your name? ")
  age = input(f"Hello, {name}. What is your age? ")
  print(f"\nHow can I help you {name}?")


greeting()


def menu():
  running = True
  print("\n1. Exit")
  print("\n2. Caculator")
  print("\n3. Rock, Paper, Scissors")
  print("\n4. N/A")
  choice = input("\n")
  if choice == "1":
    running = False
  if choice == "2":
    restart = True
    while restart:
      operation = input("\nWhat would you like to do: ")
      if "Add" in operation or "Add".lower() in operation:
        number = int(input("Your first number: "))
        number2 = int(input("Your second number: "))
        caculator(number, number2).add()
        print("Would you like to do another operation or go back to the menu?")
        choice9 = input("1. Another operation\n2. Menu\n")
        if "Menu" in choice9 or "Menu".lower() in choice9:
          menu()
          restart = False
        else:
          restart = True
      elif "Subtract" in operation or "Subtract".lower() in operation:
        number = int(input("Your first number: "))
        number2 = int(input("Your second number: "))
        caculator(number, number2).subtract()
        print("Would you like to do another operation or go back to the menu?")
        choice9 = input("1. Another operation\n2. Menu\n")
        if "Menu" in choice9 or "Menu".lower() in choice9:
          menu()
          restart = False
        else:
          restart = True
      elif "Multiply" in operation or "Multiply".lower() in operation:
        number = int(input("Your first number: "))
        number2 = int(input("Your second number: "))
        caculator(number, number2).multiply()
        print("Would you like to do another operation or go back to the menu?")
        choice9 = input("1. Another operation\n2. Menu\n")
        if "Menu" in choice9 or "Menu".lower() in choice9:
          menu()
          restart = False
        else:
          restart = True
      elif "Divide" in operation or "Divide".lower() in operation:
        number = int(input("Your first number: "))
        number2 = int(input("Your second number: "))
        caculator(number, number2).divide()
        print("Would you like to do another operation or go back to the menu?")
        choice9 = input("1. Another operation\n2. Menu\n")
        if "Menu" in choice9 or "Menu".lower() in choice9:
          menu()
          restart = False
        else:
          restart = True
  if choice == "3":
    rps()
  return running


class caculator:

  def __init__(self, num, num2):
    self.num = num
    self.num2 = num2

  def add(self):
    print(self.num + self.num2)

  def multiply(self):
    print(self.num * self.num2)

  def divide(self):
    print(self.num / self.num2)

  def subtract(self):
    print(self.num - self.num2)


def rps():
  playerpoints = 0
  cpupoints = 0
  while cpupoints < 3 and playerpoints < 3:
    player = input("Rock, Paper, or Scissors: ")
    choices = ["Rock", "Paper", "Scissors"]
    cpu = random.choice(choices)
    if player == cpu:
      print("Tie!\n")
    elif player == "Rock":
      if cpu == "Paper":
        print("You lose!\n")
        cpupoints += 1
      else:
        print("You win!\n")
        playerpoints += 1
    elif player == "Paper":
      if cpu == "Scissors":
        print("You lose!\n")
        cpupoints += 1
      else:
        print("You win!")
        playerpoints += 1
    elif player == "Scissors":
      if cpu == "Rock":
        print("You lose!\n")
        cpupoints += 1
      else:
        print("You win!\n")
        playerpoints += 1
    print(f"You have {playerpoints} points and the computer has {cpupoints} points.\n")
  if playerpoints == 3:
    print("You win.")
  elif cpupoints == 3:
    print("You lose.")
    print("Do you want to play again")

while Run:
  menu()
  Run = menu()

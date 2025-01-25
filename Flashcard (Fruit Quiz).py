import random

class FlashCard:

  def __init__(self):
    self.fruits = {
        'apple':'red',
        'banana':'yellow',
        'strawberry':'pink',
        'mango':'orange',
        'guava':'green'
    }

  def quiz(self):
    while True:
      fruit,color = random.choices(list(self.fruits.items()))[0]

      print('What is the color of {}'.format(fruit))
      user_answer=input()

      if user_answer.lower()==color:
        print("Absolutely Right !")
      else:
        print('galat jawab')

      option=int(input('enter 0 to play again 1 to exit .'))

      if option:
        break

print('Welcome to the Quiz')
fc=FlashCard()
fc.quiz()

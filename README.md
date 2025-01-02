#GUESSING GAME
import random
cnt=0
guessingNum=random.randint(1,100)
guess=int(input('Guess a number from 1 to 100 :'))
while guess!=guessingNum :
  cnt=cnt+1
  if guess<guessingNum:
    print('Too Low')
  else :
    print('Too high ')
  guess = int(input('Try again:'))

else:
  print("Exactly correct guess in",cnt,"attempts" )    

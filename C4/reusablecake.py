#Cake program
name = input('Whats your name? ')
#Prompts user's name
age = int(input('how old are you? '))
#Prompts user's age
layers = int(input('How many layers do you want? '))
#Prompts number of cake layers   
def candles(age): 
#defines function to print candles
  print(' ', end="")
#prints space for candles
for a in range (0, age, 1):
#loop for the fire on top of candle
    print(',', end="")
#prints fire on top of candles
print("") 
print(' ', end="")
for a in range(0, age, 1):
#loop for number of candles
    print('|', end="")
#prints candles

def topLayer(age):
    print("")
for a in range(0, age+2, 1):
    print(' ', end="")
#prints spaces

def base(age, layers):
    for a in range(0, layers, 1):
        print("")
#loop for number of layers\
        for a in range(0, age+2, 1):
            print('0', end="")
candles(age) #calls the candles function
topLayer(age) #calls topLayer function
base(age, layers) #calls base function
print('\n', 'Happy birthday', name, 'you are now', age, 'years old')



# class x:
#     def __init__(self):
#         print('Hi')

# y = x()

from random import choice
# hi = ['hello', 'hola', 'hi']
# user = input('enter the user name:')
# print(choice(hi)+' '+user)

# print('\u2764\uFE0F')
# import emoji

# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))

def draw_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |      
        """
    ]
    
    print(stages[6-tries])






word_list = ["apple", "banana", "cherry", "grape", "orange", "pear", "kiwi", "pineapple", "strawberry", "blueberry"]
word = choice(word_list)
# wl = len(word)b
blank = []
try_= 6
# ind = 0
for i in word:
    blank+='-'


# print(word)

while  try_:
    if '-' in blank:
        draw_hangman(try_)
        u =  input("enter :  ")
        # print(f"you still have {try_} tries ")
        
        for i in range(len(word)):
            if u[0] == word[i]:
                # ind  = u[0].index(word)
                blank[i] = u[0]
        
        if not(u[0] in word):

                try_-= 1
        print(blank)
    
    else:
        print("you won")
        break
    
if try_ == 0:
    draw_hangman(try_)
    print("Game Over")
    

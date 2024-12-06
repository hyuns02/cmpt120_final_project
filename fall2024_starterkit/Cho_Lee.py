# Language Learning App
# Jackson Lee(301619913)
# Hyunsoo Cho(301625764)
# 2024.12.05

# This line has exactly 100 characters (including the period), use it to keep each line under limit.
# We used solution draw.py

# Before testing this code, 
# ensure that the names of the functions in the cmpt120image.py file 
# match those in the solution draw.py file. 

# In our case, they didn’t match, 
# so we updated the names in the solution draw.py file 
# to match those in the cmpt120image.py file before testing.


# For exmaple, in the draw.py, we change...
# getWhiteImage -> get_white_image
# getBlackImage -> get_black_image


import pygame
import cmpt120image as img
import draw
import random

###############################################################
# Keep this block at the beginning of your code. Use caution before you modify.
# If you want to hardcode to speed up development, you can do so

# For example, set just ENV = "v" if coding in VS Code.
# You'll need to uncomment before submission!


def init_env():
    # print("\nWelcome! Before we start...")
    # env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    # while env not in "vri":
    #     print("Environment not recognized, type again.")
    #     env = input("Are you using VS Code (V), Replit (r) or IDLE (i)? ").lower()
    env = "v"
    # print("Great! Have fun!\n")
    return env

# Use the play_sound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def play_sound(soundfilename,env):
    if env == "v" or env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()
    # elif env == "r":
    #     from replit import audio
    #     audio.play_file("sounds/"+soundfilename+".wav")
ENV = init_env()
###############################################################

last_user_entry = ''

items_to_teach = 3

file = open('blackfoot.csv', 'r')
word_list = []
for word in file:
    word_list.append(word.replace('\n',''))


while last_user_entry != "quit" and last_user_entry != "4":
    print('''
MAIN MENU
1. Learn - Word Flashcards
2. Play - Seek and Find Game
3. Settings - Change Diffculty
4. Exit
    ''')
    print(f"Current settings: number of itmes to be learned is: {items_to_teach}\n")

    last_user_entry = input("Choose your option: ").strip().lower()
    print("")

    if last_user_entry == "1" or last_user_entry == "learn":
        print(f"\nLearning {items_to_teach} items!\n")
        learn_canvas = img.get_white_image(400, 400)
        learn_words_list = list(word_list[:items_to_teach])
        for words_for_learning in learn_words_list:
            item_2d_list = img.get_image(f'images/{words_for_learning}.png')
            learn_canvas = draw.distributeItems(learn_canvas, item_2d_list, 1)
            img.show_image(learn_canvas)
            play_sound(words_for_learning, ENV)
            input("Press enter to continue to the next item to be learned: ")
    
    if last_user_entry == '2' or last_user_entry == 'play':
        round = int(input("How many rounds do you want to play?: "))
        for _ in range(round):
            challenge_list = list(word_list[:items_to_teach])
            random.shuffle(challenge_list)
            challenge_list = challenge_list[:3]
            play_canvas = img.get_white_image(400, 400)
            spoken_word = random.choice(challenge_list)
            for i in range(len(challenge_list)):
                num_of_image = random.randint(1,4)
                
                if challenge_list[i] == spoken_word:
                    answer_number = num_of_image
                
                # Avoid white color 
                # because it cannot be distinguished from the canvas background color.
                r, g, b = 255, 255, 255
                while r == 255 and g == 255 and b == 255:
                    r,g,b = random.randint(0,255), random.randint(0,255), \
                        random.randint(0,255)
                
                
                play_item = img.get_image(f'images/{challenge_list[i]}.png')
                play_item = draw.recolorImage(play_item,(r, g, b))
                if random.choice([True, False]):
                    play_item = draw.mirror(play_item)
                if random.choice([True, False]):
                    play_item = draw.minify(play_item)
                play_canvas = draw.distributeItems(play_canvas, play_item, num_of_image)
            img.show_image(play_canvas)
            play_sound(spoken_word, ENV)
            
            # printing asnwer (Cheat Sheet)
            # print(f"\n** Answer: {spoken_word}, Number: {answer_number} **") 
            answer = int(input("\nHow many did you find?: "))
            
            if answer == answer_number:
                print("Correct")
            else:
                print("Wrong")

    if last_user_entry == '3' or last_user_entry == 'settings':
        print("You selected settings!")
        response = int(input(f"\nEnter a new number (between 3 and {len(word_list)}) \
for the number of itmes to learn!: "))
        while response < 3 or response > len(word_list):
            print("\nYou entered the number not in the range. Please enter a number again")
            response = int(input(f"Enter a new number (between 3 and {len(word_list)}) \
for the number of itmes to learn!: "))
        items_to_teach = response
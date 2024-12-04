import pygame
import cmpt120image as ci
import draw
import random

###############################################################
# Keep this block at the beginning of your code. Use caution before you modify.
# If you want to hardcode to speed up development, you can do so

# For example, set just ENV = "v" if coding in VS Code.
# You'll need to uncomment before submission!


def init_env():
    print("\nWelcome! Before we start...")
    # env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    # while env not in "vri":
    #     print("Environment not recognized, type again.")
    #     env = input("Are you using VS Code (V), Replit (r) or IDLE (i)? ").lower()
    env = "v"
    print("Great! Have fun!\n")
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
#ENV = initEnv()
###############################################################



file_name = ["apples", "bread", "burger", "child", "child", "coffee", "dog", "door", 
                 "eggs", "fish", "oranges", "salt", "tipi"]
items_to_teach = 3
print("MAIN MENU")
for i in range(4):
    list = ["Learn", "Play", "Settings", "Quit"]
    print(f"{i+1}. {list[i]}")
last_user_entry = input("\nChoose your option: ").strip().lower()


while last_user_entry != "quit" and last_user_entry != "4":
    if last_user_entry == "1" or last_user_entry == "learn":
        print(f"\nLearning {items_to_teach} items!")
        for _ in range(items_to_teach):
            item = random.choice(file_name)
            img = ci.get_image(f"images/{item}.png")
            sound = f"sounds/{item}.wav"

            canvas = ci.get_white_image(400, 400)
            draw.draw_item(canvas, img, random.randint(0, 300), random.randint(0, 300))
            ci.show_image(canvas)
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            input("\nPress Enter to continue...")

        
        #start implementing here
        # run_learning_part()
    elif last_user_entry == "2" or "play":
        #implement the play code here

        # create a canvas, draw it
        
        # use all the functions from draw

        # use play sound
        last_user_entry

        # etc.
    elif last_user_entry == "3" or "settings":
        #do the settings stuff
        print("give me your new setting preference...")
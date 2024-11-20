import cmpt120image
from main import init_env, play_sound
import draw

def test_play_sound(env):
    play_sound("apples", env)
    input("Press enter to continue after sound has played. ")

def test_get_image():
    cmpt120image.get_image("images/apples.png")

def test_save_image():
    my_image = cmpt120image.get_image("images/apples.png")
    cmpt120image.save_image(my_image, "copy_of_apples.png")

def test_show_image():
    my_image = cmpt120image.get_image("images/apples.png")
    cmpt120image.show_image(my_image)
    input("Press enter when done viewing image")

def test_get_black_image():
    b = cmpt120image.get_black_image(100, 100)
    cmpt120image.show_image(b)
    input("Press enter when done viewing image")

def test_get_white_image():
    w = cmpt120image.get_white_image(100, 100)
    cmpt120image.show_image(w)
    input("Press enter when done viewing image")

ENV = init_env()

def test_minify(img):
    b = cmpt120image.get_image(img)
    a = draw.minify(b)
    c =  'minified_' + img[7:]
    cmpt120image.save_image(a, c)
    cmpt120image.show_image(b)
    input("Press enter when done viewing image")
    cmpt120image.show_image(a)
    input("Press enter when done viewing image")

def test_draw_item(canvas, item, row, col):
    a = cmpt120image.get_image(canvas)
    b = cmpt120image.get_image(item)
    c = draw.draw_item(a, b, row, col)
    d = 'draw_item_' + item[7:]
    cmpt120image.save_image(c, d)
    cmpt120image.show_image(c)
    input("Press enter when done viewing image")

def create_canvas():
    canvas = cmpt120image.get_white_image(160, 160)
    cmpt120image.save_image(canvas, "canvas.png")

def get_image_size(img):
    a = cmpt120image.get_image(img)
    print(f'height: {len(a)}, width: {len(a[0])}')

# ===
# CODE TO TEST SOUNDS 
# ===
# Uncomment the below code to make sure you can play a sound!
# If this doesn't run, try to debug your error message or let the instructors know!

# test_play_sound(ENV)


# ===
# CODE TO TEST IMAGES
# ===
# screen = cmpt120image.init()

# Uncomment the below code to make sure you can get an image

# test_get_image()
# test_save_image()
# test_show_image()

# Uncomment the below code to make sure you generate "blank" black and white images

# test_get_black_image()
# test_get_white_image()



# == Code to test minifiy(img) ==
# You can test different images

# test_minify("images/child.png")


# == Code to test draw_item(canvas, item, row, col) ==
# Make sure that uncomment create_canvas function and try it first 
# before testing draw_item
# YOU NEED 'CANVAS IMAGE' FOR TESTING DRAW_ITEM

# You can test different images and locations

# create_canvas()
# test_draw_item('canvas.png', 'images/salt.png', 5, 5)


#== Code to get size of the image ==

# get_image_size('minified_child.png')
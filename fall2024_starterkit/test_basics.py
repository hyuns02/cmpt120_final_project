import cmpt120image
from fall2024_starterkit.Cho_Lee import init_env, play_sound
import fall2024_starterkit.draw1 as draw1

def test_play_sound(env):
    play_sound("apples", env)
    input("Press enter to continue after sound has played. ")

def test_get_image(img):
    cmpt120image.get_image(img)

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
    a = draw1.minify(b)
    c =  'minified_' + img[7:]
    cmpt120image.save_image(a, c)
    cmpt120image.show_image(b)
    input("Press enter when done viewing image")
    cmpt120image.show_image(a)
    input("Press enter when done viewing image")

def test_draw_item(canvas, item, row, col):
    a = cmpt120image.get_image(canvas)
    b = cmpt120image.get_image(item)
    c = draw1.draw_item(a, b, row, col)
    d = 'draw_item_' + item[7:]
    cmpt120image.save_image(c, d)
    cmpt120image.show_image(c)
    input("Press enter when done viewing image")

def create_canvas(height=160, width=160):
    canvas = cmpt120image.get_white_image(width, height)
    cmpt120image.save_image(canvas, "canvas.png")

def get_image_size(img):
    a = cmpt120image.get_image(img)
    print(f'height: {len(a)}, width: {len(a[0])}')

def test_mirror(img):
    a = cmpt120image.get_image(img)
    c = draw1.mirror(a)
    d = 'mirror_' + img[7:]
    cmpt120image.save_image(c, d)
    cmpt120image.show_image(a)
    input("Press enter when done viewing image")
    cmpt120image.show_image(c)
    input("Press enter when done viewing image")

def test_recolor(img, color):
    b = cmpt120image.get_image(img)
    a = draw1.recolor_image(b, color)
    c =  'recolor_' + img[7:]
    cmpt120image.save_image(a, c)
    cmpt120image.show_image(a)
    input("Press enter when done viewing image")

def test_distribute_items(canvas, item, n):
    a = cmpt120image.get_image(canvas)
    b = cmpt120image.get_image(item)
    c = draw1.distribute_items(a, b, n)
    d = 'distri_items_' + item[7:]
    cmpt120image.save_image(c, d)
    cmpt120image.show_image(c)
    input("Press enter when done viewing image")

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


# == Code to test recolor(img, color) ==
# test_recolor('images/oranges.png', (255,0,255))


# == Code to test minifiy(img) ==
# You can test different images

# test_minify("images/tipi.png")


# == Code to test mirror(img) ==
# test_mirror('images/coffee.png')


# == Code to test draw_item(canvas, item, row, col) ==
# Make sure that uncomment create_canvas function and try it first 
# before testing draw_item
# YOU NEED 'CANVAS IMAGE' FOR TESTING DRAW_ITEM

# You can test different images and locations

# create_canvas(320, 320)
# test_draw_item('canvas.png', 'images/door.png', 60, 60)


# == Code to test dritribute_items functions ==
# test_distribute_items('canvas.png', 'images/child.png', 4)


#== Code to get size of the image ==
# get_image_size('minified_tipi.png')

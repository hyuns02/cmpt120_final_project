# Image Processing Module
# Jackson Lee(301619913)
# Hyunsoo Cho(301625764)
# 2024.11.22

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120image as ci
ci.init()

def colour_check(pixcel):
  r,g,b = pixcel
  if r == 0 and g == 0 and b == 0:
    return True
  else:
    return False


# Note: delete all `return False` lines as you complete each function!
def recolor_image(img, color):
  height = len(img)
  width = len(img[0])
  child = ci.get_image("child.png")

  for row in range(height):
    for col in range(width):
      pixcel_from_image = child[row][col]
      if colour_check(pixcel_from_image):
        child[row][col] = color
        ci.get_white_image
  return child

  # ci.show_image(child, "merged")
  # input("Please any key to end to process")


def minify(img):
  # Get height and width of the img and create canvas
  img_height = len(img)
  img_width = len(img[0])
  result_image = ci.get_white_image(img_width, img_height)

  
  # Reduce both height and width
  for row in range(0,img_height,2):
    for col in range(0,img_width,2):
      list_of_rgb = []
      for i in range(3):
        avg = int((img[row][col][i] + img[row][col+1][i] + 
                   img[row+1][col][i] + img[row+1][col+1][i])/4)
        list_of_rgb.append(avg)
      result_image[row//2][col//2] = list_of_rgb
  return result_image

def mirror(img):
  height = len(img)
  
def draw_item(canvas, item, row, col):
  # Get height and width of the item
  item_height = len(item)
  item_width = len(item[0])
  
  # Locate item on canvas and replace pixels of canvas to pixels of item
  for r in range(row, row+item_height):
    for c in range(col, col+item_width):
      canvas[r][c] = item[r-row][c-col]
  return canvas
  
def distribute_items(canvas, item, n):
  # Add your code here
  return False

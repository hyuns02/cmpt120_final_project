# Image Processing Module
# Jackson Lee(301619913)
# Hyunsoo Cho(301625764)
# 2024.11.22

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120image as ci
import random
ci.init()

# check if the color of the pixel is non-white
def color_check(pixel):
  r,g,b = pixel
  return r != 255 and g != 255 and b != 255

def recolor_image(img, color):
  # Get height and width of the img and create canvas
  img_height = len(img)
  img_width = len(img[0])
  result_img = ci.get_white_image(img_width,img_height)

  # Change the color of the pixel if the color is non-white into color that user want
  for row in range(img_height):
    for col in range(img_width):
      if color_check(img[row][col]):
        result_img[row][col] = color
      else:
        result_img[row][col] = img[row][col]
  return result_img

def minify(img):
  # Get height and width of the img and create canvas
  img_height = len(img)
  img_width = len(img[0])
  result_img = ci.get_white_image(img_width//2, img_height//2)

  # Reduce both height and width
  for row in range(0,img_height,2):
    for col in range(0,img_width,2):
      pixel = []
      for i in range(3):
        avg = (img[row][col][i] + img[row][col+1][i] + 
                   img[row+1][col][i] + img[row+1][col+1][i])//4
        pixel.append(avg)
      result_img[row//2][col//2] = pixel
  return result_img

def mirror(img):
  # Get height and width of the img and create canvas
  img_height = len(img)
  img_width = len(img[0])
  result_img = ci.get_white_image(img_width, img_height)

# mirroring the image
  for row in range(img_height):
    for col in range(img_width):
      opposite_col = img_width - col - 1
      result_img[row][col] = img[row][opposite_col]
  return result_img


def draw_item(canvas, item, row, col):
  # Get height and width of the item
  item_height = len(item)
  item_width = len(item[0])
  
  # Locate item on canvas and replace pixels of canvas to pixels of item
  for r in range(row, row+item_height):
    for c in range(col, col+item_width):
      if color_check(item[r-row][c-col]):
        canvas[r][c] = item[r-row][c-col]
  return canvas
  
def distribute_items(canvas, item, n):
  # Get height and width of canvas and item
  canvas_height = len(canvas)
  canvas_width = len(canvas[0])
  item_height = len(item)
  item_width = len(item[0])
  
  # Draw item n times on random location of canvas using draw item function
  for _ in range(n):
    row = random.randint(0,canvas_height-item_height+1)
    col = random.randint(0,canvas_width-item_width+1)
    draw_item(canvas, item, row, col)
  return canvas

# Image Processing Module
# Jackson Lee(301619913)
# Hyunsoo Cho(301625764)
# 2024.11.22

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120image as ci
ci.init()

# check if the colour of the pixcel is black
def colour_check(pixcel):
  r,g,b = pixcel
  return r == 0 and g == 0 and b == 0

def recolor_image(img, color):
  height = len(img)
  width = len(img[0])
  photo = ci.get_image(img)

# changing the colour of the pixcel if the colour is black into colour that user want
  for row in range(height):
    for col in range(width):
      pixcel_from_image = photo[row][col]
      if colour_check(pixcel_from_image):
<<<<<<< HEAD
        photo[row][col] = color
=======
        child[row][col] = color
        ci.get_white_image
  return child

  # ci.show_image(child, "merged")
  # input("Please any key to end to process")
>>>>>>> ea0d240632a762669fc9561763749dde43973d5a

# creating the new photo with changed colour
  result_img = ci.get_white_image()
  for row in range(height):
      for col in range(width):
        result_img[row][col] = photo[row][col]
  return result_img
  

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
<<<<<<< HEAD

  # Creating the new image
  result_image = ci.get_white_image(width//2,height//2)
  for row in range(height//2):
    for col in range(width//2):
      result_image[row][col] = result[row][col]
=======
      result_image[row//2][col//2] = list_of_rgb
>>>>>>> ea0d240632a762669fc9561763749dde43973d5a
  return result_image

def mirror(img):
  height = len(img)
  width = len(img[0])
  photo = ci.get_image(img)
# mirroring the photo
  for row in range(height):
    for col in range(width // 2):
      opposite_col = width - col - 1
      photo[row][col], photo[row][opposite_col] = photo[row][opposite_col], photo[row][col]

# creating new reult img 
  result_img = ci.get_white_image()
  for row in range(height):
    for col in range(width):
      result_img[row][col] = photo[row][col]
  return result_img


  
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

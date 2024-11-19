# Your header

import cmpt120image
cmpt120image.init()


# Note: delete all `return False` lines as you complete each function!
def recolor_image(img, color):
  # Add your code here
  return False

def minify(img):
  # Get height and width of the img
  height = len(img)
  width = len(img[0])
  
  # Reduce both height and width
  result = []
  for row in range(0,height,2):
    list_of_pixel = []
    for col in range(0,width,2):
      list_of_rgb = []
      for i in range(3):
        avg = int((img[row][col][i] + img[row][col+1][i] + 
                   img[row+1][col][i] + img[row+1][col+1][i])/4)
        list_of_rgb.append(avg)
      list_of_pixel.append(list_of_rgb)
    result.append(list_of_pixel)

  # Create new image
  result_image = cmpt120image.get_white_image(width//2,height//2)
  for row in range(height//2):
    for col in range(width//2):
      result_image[row][col] = result[row][col]
  return result_image

def mirror(img):
  # Add your code here
  return False
  
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

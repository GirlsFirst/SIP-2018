from PIL import Image
import math

# Return an Image loaded from the specified file.
#  * filename: string, name of file to load
def load_img(filename):
  im = Image.open(filename)
  return im

# Display Image to the user (for debugging purposes).
#   * im: Image to display
def show_img(im):
  im.show()

# Save the Image to a file with the specified filename,
#  then show the Image to the user.
#  * im: Image to be saved
#  * filename: string, name to save file as
def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

# Return a new Image, with Obamicon filter applied.
#  * im: Image to be filtered
def obamicon(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Define color constants to use for recoloring.
  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)

  # Process the pixels in the image.
  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Return a new Image, with grayscale filter applied.
#  * im: Image to be filtered
def grayscale(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Process the pixels in the image.
  for p in pixels:
    new_p = avg_pixel(p)
    new_pixels.append(new_p)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Return a sequence of pixels, with emphasize filter applied.
#  * im: Image to be filtered
#  * rgb_color: (r,g,b) tuple, color to be isolated in image
#  * threshold: int, tolerance for which colors should be filtered
def emphasize(im, rgb_color, threshold):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Set RGB values for color to isolate in the image
  rtarget = rgb_color[0]
  gtarget = rgb_color[1]
  btarget = rgb_color[2]

  # Process the pixels in the image.
  for p in pixels:
    r = p[0]
    g = p[1]
    b = p[2]

    # Calculate how far away p's color is from the target color.
    #  Use the distance formula:
    #  d = sqrt((rtarget-r)^2 + (gtarget-g)^2 + (btarget-b)^2)
    color_dist = math.sqrt((rtarget-r)**2 + (gtarget-g)**2 + (btarget-b)**2)

    # If p's color is too far away from target color,
    #  make it grayscale. Otherwise, use p's color.
    if color_dist > threshold:
      new_p = avg_pixel(p)
      new_pixels.append(new_p)
    else:
      new_pixels.append(p)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Return a new Image, with add_color filter applied.
#  * im: Image to be filtered
#  * color: (r,g,b) tuple
def add_color(im, color):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Process the pixels in the image.
  for p in pixels:
    new_r = p[0]+color[0]
    new_g = p[1]+color[1]
    new_b = p[2]+color[2]
    new_pixels.append((new_r, new_g, new_b))

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Return a new Image, with invert filter applied.
#  * im: Image to be filtered
def invert(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Process the pixels in the image.
  for p in pixels:
    new_r = 255-p[0]
    new_g = 255-p[1]
    new_b = 255-p[2]
    new_pixels.append((new_r, new_g, new_b))

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Helper function.
# Return a grayscale tuple for a single pixel value.
#  * pixel: (r,g,b) tuple
def avg_pixel(pixel):
  # Use the average of p's RGB values to set a new pixel value.
  avg = (pixel[0] + pixel[1] + pixel[2]) // 3 # Use // for int division.
  return (avg, avg, avg) # R = G = B will be a gray pixel!
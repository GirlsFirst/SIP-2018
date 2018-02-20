from PIL import Image
import math

# Return a sequence of pixels, with Obamicon filter applied.
def obamicon(pixels):
  # Define color constants to use for recoloring.
  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)

  # Create a list to hold the new image pixel data.
  new_pixels = []

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

  return new_pixels

# Return a sequence of pixels, with grayscale filter applied.
def grayscale(pixels):
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Process the pixels in the image.
  for p in pixels:
    new_p = avg_pixel(p)
    new_pixels.append(new_p)

  return new_pixels

# Return a sequence of pixels, with emphasize filter applied.
def emphasize(pixels, rgb_color, threshold):
  rtarget = rgb_color[0]
  gtarget = rgb_color[1]
  btarget = rgb_color[2]

  # Create a list to hold the new image pixel data.
  new_pixels = []

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

  return new_pixels

# Return a sequence of pixels, with add_color filter applied.
def add_color(pixels, color):
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Process the pixels in the image.
  for p in pixels:
    new_r = p[0]+color[0]
    new_g = p[1]+color[1]
    new_b = p[2]+color[2]
    new_pixels.append((new_r, new_g, new_b))

  return new_pixels

# Return a grayscale tuple for a single pixel value.
def avg_pixel(pixel):
  # Use the average of p's RGB values to set a new pixel value.
  avg = (pixel[0] + pixel[1] + pixel[2]) // 3 # Use // for int division.
  return (avg, avg, avg) # R = G = B will be a gray pixel!

def main():
  # Load the image from a file.
  im = Image.open("brooklyn.jpg")
  pixels = im.getdata()

  newim = Image.new("RGB", im.size)

  # Calculate the Obamicon filter!
  obamicon_pixels = obamicon(pixels)
  # Save the recolored pixels to a new image.
  newim = Image.new("RGB", im.size)
  newim.putdata(obamicon_pixels)
  newim.save("recolored_obamicon.jpg", "jpeg")
  newim.show()# Display the new image to the user.

  # Calculate the grayscale filter!
  grayscale_pixels = grayscale(pixels)
  # Save the recolored pixels to a new image.
  newim.putdata(grayscale_pixels)
  newim.save("recolored_grayscale.jpg", "jpeg")
  newim.show() # Display the new image to the user.

  # Calculate the emphasize filter!
  emphasize_pixels = emphasize(pixels, (189, 136, 87), 100)
  # Save the recolored pixels to a new image.
  newim.putdata(emphasize_pixels)
  newim.save("recolored_emphasize.jpg", "jpeg")
  newim.show() # Display the new image to the user.

  # Calculate the add_color filter!
  add_color_pixels = add_color(pixels, (0, 30, 0))
  # Save the recolored pixels to a new image.
  newim.putdata(add_color_pixels)
  newim.save("recolored_add_color.jpg", "jpeg")
  newim.show() # Display the new image to the user.

if __name__ == "__main__":
  main()
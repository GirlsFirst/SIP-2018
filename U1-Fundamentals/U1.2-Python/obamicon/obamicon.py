from PIL import Image

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


def main():
  # Load the image from a file.
  im = Image.open("brooklyn.jpg")
  pixels = im.getdata()

  # Calculate the Obamicon filter!
  new_pixels = obamicon(pixels)

  # Save the recolored pixels to a new image.
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  newim.save("recolored.jpg", "jpeg")

  newim.show() # Display the new image to the user.

if __name__ == "__main__":
  main()
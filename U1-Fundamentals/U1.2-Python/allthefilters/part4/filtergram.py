import filters

def main():
  # Ask what image the user wants to edit
  filename = input("Enter the name of the image file to edit: ")
  
  # Load the image from the specified file
  img = filters.load_img(filename)

  # Apply filters!
  newimg = filters.obamicon(img)
  newimg = filters.grayscale(newimg)

  blue = (30,85,115)
  anotherimg = filters.emphasize(img, blue, 50)

  blueimg = filters.add_color(img, blue)

  lastimg = filters.invert(blueimg)

  # Save the final images
  filters.save_img(newimg, "recolored1.jpg")
  filters.save_img(anotherimg, "recolored2.jpg")
  filters.save_img(blueimg, "recolored3.jpg")
  filters.save_img(lastimg, "recolored4.jpg")

if __name__ == '__main__':
  main()
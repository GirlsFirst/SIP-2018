import filters

def main():
  # Ask what image the user wants to edit
  filename = input("Enter the name of the image file to edit: ")
  
  # Load the image from the specified file
  img = filters.load_img(filename)

  # Apply filters!
  newimg = filters.obamicon(img)
  newimg = filters.grayscale(newimg)

  # Save the final image
  filters.save_img(newimg, "recolored.jpg")

if __name__ == '__main__':
  main()
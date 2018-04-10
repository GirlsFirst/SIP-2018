import filters

def main():
  # Ask what image the user wants to edit
  filename = input("Enter the name of the image file to edit: ")
  
  # Load the image from the specified file
  img = filters.load_img(filename)

  # Save the final image
  filters.save_img(img, "recolored.jpg")

if __name__ == '__main__':
  main()
# MINI-PROJECT 1. PHOTO EDITOR.

from PIL import Image, ImageFilter

name = input("IMAGE NAME(e.g. photo.jpg):")
img = Image.open(name)

while True:
    print ("\n--- PHOTO EDITOR ---")
    print("1. Black & White")
    print("2. Blur")
    print("3. Rotate")
    print("4. Small Size")
    print("5. Sketch")
    print("6. Exit")

    choice = input("Choose:")

    if choice == "1":
        new = img.convert("L")

    elif choice == "2":
        blur = ImageFilter.GaussianBlur(5)
        new = img.filter(blur)

    elif choice == "3":
        new = img.rotate(90, expand=True)

    elif choice == "4":
        W,h = img.size
        new = img.resize((W//2,h//2))

    elif choice == "5":
        new = img.filter(ImageFilter.CONTOUR)

    elif choice == "6":
        img.save("edited_photo.png")
        print("BYE!")
        break

    else:
        print("wrong choice")
        continue

    img = new
    print("Effects applied successfully")
"""
Numpy Image Editor
a program to edit images using NumPy and PIL.
Supports operations: Grayscale, Brightness, Flip, Crop, Rotate, and more.
"""

import numpy as np
from PIL import Image,ImageFilter

class ImageEditor:
    """A class for loading, editing, and saving images using NumPy and PIL"""
    def __init__(self):
        """Initialize the ImageEditor with an empty image array"""
        self.img_array=None

    def img_loading(self):
        """Load an image from a user-provided path and convert it to a NumPy array"""
        img_path=input("Please Enter Your Image Path:")
        img_path=img_path.strip().strip('"').strip("'")
        try:
            img=Image.open(img_path)
            self.img_array=np.array(img)
            return self.img_array
        except (FileNotFoundError, OSError):
            print("Image doesn't Exist on Your Device! Try Again!")
            return None

    def display_image(self):
        """Display the current image using the default image viewer"""
        Image.fromarray(self.img_array).show()
#1
    def show_img_info(self):
        """Print information about the current image (dimensions, size, channels, dtype)"""
        print("------Your Image Information------")
        print(f"""\tImage Dimensions: {self.img_array.ndim}
            Image Size: {self.img_array.size}
            Image Height: {self.img_array.shape[0]}
            Image Width: {self.img_array.shape[1]}
            Image Channels: {self.img_array.shape[2]}
            Data type: {self.img_array.dtype}\n""")
#2
    def convert_to_grayscale(self):
        """Convert the image to grayscale using weighted RGB values"""
        gray=np.dot(self.img_array[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
        self.img_array=gray
#3
    def increase_brightness(self,value=50):
        """Increase the brightness of the image by a given value"""
        img=self.img_array.astype(np.int16)+value
        img=np.clip(img, 0, 255)
        self.img_array=img.astype(np.uint8)
#4
    def decrease_brightness(self,value=50):
        """Decrease the brightness of the image by a given value"""
        img=self.img_array.astype(np.int16)-value
        img=np.clip(img, 0, 255)
        self.img_array=img.astype(np.uint8)
#5
    def flip_horizontal(self):
        """Flip the image horizontally (mirror effect)"""
        self.img_array=self.img_array[:,::-1]
#6
    def flip_vertical(self):
        """Flip the image vertically (upside down)"""
        self.img_array=self.img_array[::-1,:]
#7
    def crop(self):
        """Crop the image based on user-defined boundaries (rows and columns)"""
        height=self.img_array.shape[0]
        width=self.img_array.shape[1]
        print(f"Your image size: Height={height} pixels | Width={width} pixels")
        print("You'll define the area to crop using 4 numbers (the box boundaries):")
        y1 = int(input(f"\tStart row from the top(enter a number between 0 and {height}): "))
        y2 = int(input(f"\tEnd row(enter a number between {y1} and {height}): "))
        x1 = int(input(f"\tStart column from the left(enter a number between 0 and {width}): "))
        x2 = int(input(f"\tEnd column(enter a number between {x1} and {width}): "))

        if x2<=x1 or y2<=y1:
            print("\nInvalid numbers! The end value must be greater than the start value!\n")
            return False

        if y2>height or x2>width:
            print("\nThese numbers exceed the image size!")
            print("Maximum Height={height}, and Maximum Width={width}\n")
            return False

        print(f"\nCropping from (row {y1}, column {x1}) to (row {y2}, column {x2})")
        self.img_array=self.img_array[y1:y2,x1:x2]
        return True
#8
    def negative(self):
        """Apply a negative filter to the image (invert colors)"""
        self.img_array=255-self.img_array
#9
    def rotate(self):
        """Rotate the image by 90, 180, or 270 degrees based on user input"""
        print("""\tRotation options:
            1. Rotate 90 degrees
            2. Rotate 180 degrees
            3. Rotate 270 degrees""")
        option=int(input("Enter an option: "))
        if option==1:
            self.img_array=np.rot90(self.img_array,k=1)
            return True
        if option==2:
            self.img_array=np.rot90(self.img_array,k=2)
            return True
        if option==3:
            self.img_array=np.rot90(self.img_array,k=3)
            return True
        else:
            print("Invalid Option!\n")
            return False
#10
    def black_and_white_img(self):
        """Convert the image to pure black and white using a threshold"""
        self.convert_to_grayscale()
        gray=self.img_array
        img=np.where(gray>128,255,0)
        self.img_array=img.astype(np.uint8)
#11
    def resize_image(self):
        """Resize the image to new dimensions provided by the user"""
        new_height=int(input("Enter The New Height: "))
        new_width=int(input("Enter The New Width: "))

        if new_height>0 and new_width>0 :
            img=Image.fromarray(self.img_array)
            new_image=img.resize((new_width,new_height))
            self.img_array=np.array(new_image)
            return True
        else:
            print("Dimensions must be Greater Than 0!")
            return False
#12
    def blur_image(self):
        """Apply Gaussian blur to the image with user-defined intensity"""
        img=Image.fromarray(self.img_array)
        rd=int(input("Enter blur intensity(1:10): "))
        new_img=img.filter(ImageFilter.GaussianBlur(radius=rd))
        self.img_array=np.array(new_img)

#13
    def save_image(self):
        """Save the current image to a file with a user-provided name"""
        filename=input("Enter The file name(.jpg/.png): ").strip().strip("'").strip('"')
        if not (filename.endswith(".jpg") or filename.endswith(".png")):
            filename+=".png"
        Image.fromarray(self.img_array).save(filename)
        print("Image Saved Successfully!")


#----------------------------Menu--------------------------------
    def run(self):
        """Run the interactive menu-driven image editor"""
        print("====Welcome To Numpy Image Editor====")
        counter=0
        while self.img_loading() is None:
            pass
        self.display_image()
        while True:
            print("""\tMain Menu:
                  1. Show Image Info.
                  2. Convert to Grayscale
                  3. Increase Brightness
                  4. Decrease Brightness
                  5. Flip Horizontally
                  6. Flip Vertically
                  7. Crop Image
                  8. Negative Image
                  9. Rotate Image
                  10. Black & White Image
                  11. Resize Image
                  12. Blur Image
                  13. Save Image
                  14. Exit""")
            option=int(input("Enter Your Option: "))
            if option==1:
                self.show_img_info()
            elif option==2:
                self.convert_to_grayscale()
                print("The Image has been Converted To Grayscale!\n")
                counter+=1
                self.display_image()
            elif option==3:
                value=int(input("Enter a Value: "))
                self.increase_brightness(value)
                counter+=1
                self.display_image()
            elif option==4:
                value=int(input("Enter a Value: "))
                self.decrease_brightness(value)
                counter+=1
                self.display_image()
            elif option==5:
                self.flip_horizontal()
                counter+=1
                self.display_image()
            elif option==6:
                self.flip_vertical()
                counter+=1
                self.display_image()
            elif option==7:
                success=self.crop()
                if success:
                    counter+=1
                    self.display_image()
            elif option==8:
                self.negative()
                counter+=1
                self.display_image()
            elif option==9:
                success=self.rotate()
                if success:
                    counter+=1
                    self.display_image()
            elif option==10:
                self.black_and_white_img()
                counter+=1
                self.display_image()
            elif option==11:
                success=self.resize_image()
                if success:
                    counter+=1
                    self.display_image()
            elif option==12:
                self.blur_image()
                counter+=1
                self.display_image()
            elif option==13:
                self.save_image()
            elif option==14:
                print("Thanks For Trying Numpy Image Editor♡")
                saving_choice=input("Did you save the image? (Y/N) : ").strip().lower()
                if saving_choice!="y":
                    s_choice=input("Do You Want To Save The Image? (Y/N) : ").strip().lower()
                    if s_choice=="y":
                        self.save_image()

                if counter>1:
                    print(f"You have made {counter} edits to your Image.")
                elif counter==1:
                    print(f"You have made {counter} edit to your Image.")
                else:
                    print("You havn\'t made any edits to your Image.")

                print("Good Bye☆")
                break
            else:
                print("It\'s Not an Option! Try Again!")


if __name__ == "__main__":
    editor=ImageEditor()
    editor.run()

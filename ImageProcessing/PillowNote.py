from PIL import Image, ImageFilter
import os                            #? Import the os module to interact with the operating system




#TODO - Basic Image Operations
# image1 = Image.open("cat.4001.jpg")  #? Open an image file
# image1.show()                        #? Display the image
# image1.save("cat_copy.png")          #? Save the image in a different format



#TODO - Convert all JPG images in the current directory to PNG format and save them in a folder named 'pngs'
# for file in os.listdir():                       #! Loop through all files in the current directory
#     if file.endswith(".jpg"):
#         image = Image.open(file)                #? Open each JPG image file in the current directory    
#         Filemame, ext = os.path.splitext(file)  #? Split the filename and extension
#         image.save(f'pngs/{Filemame}.png')      #? Save the image in 'pngs' folder with .png extension



#TODO - resize an image
# size_300 = (300, 300)                   #? Define a tuple for the new size
# size_700 = (700, 700)                   #? Define a tuple for the new size

# for file in os.listdir():                       #! Loop through all files in the current directory
#     if file.endswith(".jpg"):
#         image = Image.open(file)                         #? Open each JPG image file in the current directory    
#         Filemame, ext = os.path.splitext(file)           #? Split the filename and extension

#         image.thumbnail(size_700)                        #? Resize the image to 300x300 pixels using thumbnail() method which maintains aspect ratio
#         image.save(f'Size700/{Filemame}_700x700.jpg')    #? Save the resized image in 'resized' folder

#         image.thumbnail(size_300)                        #? Resize the image to 700x700 pixels using thumbnail() method which maintains aspect ratio
#         image.save(f'Size300/{Filemame}_300x300.jpg')    #? Save the resized image in 'resized' folder



#TODO - Apply filters to images

image1 = Image.open("cat.4001.jpg")          
#image1.rotate(90).show()                           #? Rotate the image by 90 degrees and display it
#image1.filter(ImageFilter.GaussianBlur(15)).show() #? Apply a Gaussian blur filter to the image and display it
#image1.filter(ImageFilter.CONTOUR).show()          #? Apply a contour filter to the image and display it
#image1.convert("L").show()                         #? Convert the image to grayscale and display it
#image1.filter(ImageFilter.DETAIL).show()           #? Apply a detail filter to the image and display it
#image1.filter(ImageFilter.EDGE_ENHANCE).show()     #? Apply an edge enhance filter to the image and display it
#image1.filter(ImageFilter.EMBOSS).show()           #? Apply an emboss filter to the image and display it
#image1.filter(ImageFilter.SHARPEN).show()          #? Apply a sharpen filter to the image and display it
#image1.filter(ImageFilter.SMOOTH).show()           #? Apply a smooth filter    
#image1.transpose(Image.FLIP_LEFT_RIGHT).show()     #? Flip the image horizontally and display it
#image1.transpose(Image.FLIP_TOP_BOTTOM).show()     #? Flip the image vertically
#image1.transpose(Image.ROTATE_180).show()          #? Rotate the image by 180 degrees and display it























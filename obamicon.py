from PIL import Image


#function
def changing(colorlist):
    newlist = []
    for counter in colorlist:
        intensity = counter[0] + counter[1] + counter[2]
        if intensity < 182:
            newlist.append(darkBlue)
        elif intensity < 364:
            newlist.append(red)
        elif intensity < 546:
            newlist.append(lightBlue)
        else:
            newlist.append(yellow)
    return newlist


# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
myimage = Image.open("puppy.jpeg") #change IMAGENAME to the path on your computer to the image you're using
imagelist = myimage.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
imagelist = list(imagelist) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = changing(imagelist) #list that will hold the pixel data for the new image.
print(recolored)

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



# Create a new image using the recolored list. Display and save the image.
newimage = Image.new("RGB", myimage.size) #Creates a new image that will be the same size as the original image.
newimage.putdata(recolored) #Adds the data from the recolored list to the image.
newimage.show() #show the new image on the screen
newimage.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

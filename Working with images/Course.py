from PIL import Image

mac = Image.open('example.jpg')

#mac.size

#mac.filename
#mac.format_description

#cropping images:
mac.crop((0,0,100,100)) #top left cornet

pencils = Image.open('pencils.png')
pencils.size
x=0
y=0

w = 1950/3
h=1300/10

pencils.crop((x,y,w,h)) #from the top left corner

x=0
y-1100

w= 1950/3
h=1300
pencils.crop((x,y,w,h)) #Bottom

computer = pencils.crop((x,y,w,h))
mac.paste(im=computer, box =(0,0)) #to paste the image on the original picture

mac.resize((3000, 500)) #set the new size

mac.rotate(90) #rotate the image

#Color transparency

red = Image.open('red_color.jpeg')
blue = Image.open('blue_color.jpeg')

blue.putalpha (0)  #0 is fully transparent

blue.paste(im=red, box=(0.0), mask=red)
blue #we obtain purple

blue.save("purple.png") #to save the new image
purple = Image.open("purple.png")
purple #open the file


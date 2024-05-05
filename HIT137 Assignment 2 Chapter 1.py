#Chapter 1 



from PIL import Image
#load the image
image = Image.open("/Users/ashrietalipuan/Desktop/chapter1.jpg")


#generate a number
import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)
#process each pixel in the image
width, height = image.size
for x in range(width):
    for y in range(height):
        #Get the original pixel value
        r, g, b = image.getpixel((x, y))
        
        #Add the generated number to each RGb component
        new_r = min(r + generated_number, 300)
        new_g = min(g + generated_number, 300)
        new_b = min(b + generated_number, 300)
        
        #Update the pixel with the new values
        image.putpixel((x,y)), (new_r, new_g, new_b)

#Save the modified image
image.save(chapter1out.jgp)







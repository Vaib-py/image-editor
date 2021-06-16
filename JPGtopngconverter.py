from PIL import Image
import os
import sys
# JPG TO PNG CONVERTER

#grab first and sec argument

img_fol = sys.argv[1]
final_fol = sys.argv[2]

# Check if new fol exists,if not creat it bro

if not os.path.exists(final_fol):
    os.makedirs(final_fol)
    
# Convert them into png bro
    
for filename in os.listdir(img_fol):
    img = Image.open (f"{img_fol}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save (f'{final_fol}{clean_name}.png','png')
    print ('All done boi')

    
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import img2pdf 
from PIL import Image 
import os 
import tkinter.filedialog

# This will brows the file
img_path=tkinter.filedialog.askopenfilename()

  
# storing pdf path 
brows_pdf_path = "File path"
  
# opening image 
image = Image.open(brows_pdf_path) 
  
# converting into chunks using img2pdf 
pdf_bytes = img2pdf.convert(image.filename) 
  
# opening or creating pdf file 
file = open(brows_pdf_path, "wb") 
  
# writing pdf files with chunks 
file.write(pdf_bytes) 
  
# closing image file 
image.close() 
  
# closing pdf file 
file.close() 
  
# output 
print("Successfully") 


# In[ ]:





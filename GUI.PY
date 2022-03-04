import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pandas as pd
import cv2
from PIL import Image
import img2pdf
import os
from datetime import date
  
  
# Returns the current local date
today = date.today()
today = date.today()
my_w = tk.Tk()
my_w.geometry("800x800")  # Size of the window 
my_w.title('Certificates Maker')
my_font1=('times', 20, 'bold')
l1 = tk.Label(my_w,text='Upload CSV File and Template In a Order & Generate Certificates',width=50,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload Files', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 


def upload_file():
    file = filedialog.askopenfilename()
    img_file = filedialog.askopenfilename()
    data=pd.read_csv(file)
    details =  data.to_dict('records')
    Total_Certificates=len(details)
   
    
    for i in range(Total_Certificates):
        im = cv2.imread(img_file)
        Name=details[i]["Name"]
        #Length of Name for example if name is "Sachin Tendulkar" then length is 16
        Length_of_Name=len(Name)
        Program_Name=details[i]["Project"]
        # Similarly length of Program Name
        Length_of_Program=len(Program_Name)

         # choose the font from opencv
        font = cv2.FONT_HERSHEY_TRIPLEX 
        #Image width and height
        w,h,c=im.shape
        w_n=(w+Length_of_Name)//2
        w_p=(w+Length_of_Program)//2
    
        
        # Position of Name, Program Name and Date
        org1 = (w_n+300, 560)
        org2 = (w_p+300, 750)
        org3 = (970, 1100)
        
        # fontScale
        fontScale = 2
        
        # Black color in BGR
        color = (0, 0, 0)
        
        # Line thickness of 6 px
        thickness = 6
        
        # Using cv2.putText() method
        image = cv2.putText(im, str(details[i]["Name"]), org1, font, 
                        fontScale, color, thickness, cv2.LINE_AA)
        image = cv2.putText(im, str(details[i]["Project"]), org2, font, 
                        fontScale, color, thickness, cv2.LINE_AA)    
        image = cv2.putText(im, str(today), org3, font, 
                        fontScale, color, thickness, cv2.LINE_AA)                              
        filename = str(i)+'.jpg'
        try:
            os.mkdir(str(i))
        except:
            pass
        
        cv2.imwrite(str(i)+"/"+filename, image)
        import glob
        with open(str(i)+".pdf", "wb") as f:
            f.write(img2pdf.convert([i for i in glob.glob(str(i)+"/*.jpg")]))
    #file = filedialog.askopenfile()
    #print(file.read())
my_w.mainloop()  # Keep the window open
import numpy
import numpy as np
#from keras.models import load_model
#from keras.preprocessing import image
import csv
#from keras import models
from tkinter import *
from tkinter import filedialog, scrolledtext, messagebox

from PIL import Image
import glob
image_list = []

root = Tk()
root.title("Flowers4U")
root.geometry('660x400')



def close_window():
    root.destroy()

def BrowseFile():
    global sourceFile
    sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a file')
    e1.delete(0, END)
    e1.insert(0,sourceFile)

def BrowseFolder():
    global sourceFolder
    sourceFolder = filedialog.askdirectory(parent=root, initialdir= "/", title='Please select a directory')
    e2.delete(0, END)
    e2.insert(0,sourceFolder)


def writTofile(str):
    a=str.split(" - ")[0]
    b = str.split(" - ")[1]
    row=[a,b]
    with open('result.csv', 'a',newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    pass


# def predict():
#     if e1.get()=="":
#         messagebox.showwarning('Error', 'please select a model file')  # shows warning message
#     elif e2.get() == "":
#         messagebox.showwarning('Error', 'please select a folder for images')  # shows warning message
#     else:
#         image_list = []
#         for filename in glob.glob(e2.get()+'\\*.jpg'):  # assuming gif
#             im = Image.open(filename)
#             image_list.append(im)
#
#         model=load_model(e1.get())
#         loss = 'categorical_crossentropy'
#         model.compile(loss=loss, optimizer='adam', metrics=['accuracy'])
#         for im in image_list:
#             test_image = image.load_img(im.fp.name, target_size=(128, 128,3))
#             test_image = image.img_to_array(test_image)
#             test_image = numpy.expand_dims(test_image, axis=0)
#             #test_image = test_image.reshape(128, 128)
#             result = model.predict(test_image)
#             str = im.fp.name.split("\\")[1]+ " - "
#             if result[0][0]==1.0:
#                 str += "daisy"
#             elif result[0][1] == 1.0:
#                 str += "dandelion"
#             elif result[0][2] == 1.0:
#                 str += "rose"
#             elif result[0][3] == 1.0:
#                 str += "sunflower"
#             elif result[0][4] == 1.0:
#                 str += "tulip"
#             print(str)
#             writTofile(str)
#             txt.insert(INSERT, str+"\n")
#

def clear():
    txt.delete(1.0, END)

lbl1 = Label(root, text="Select file of trained model ")
lbl1.grid(column=0, row=0)

lbl2 = Label(root, text="Select folder that contains images ")
lbl2.grid(column=0, row=1)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

#browse to selected trained file model
button1 = Button(root, text="Browse", command=BrowseFile)
button1.grid(column=1, row=0, padx = 22, pady=10)

#browse folder for images
button2 = Button(root, text="Browse", command=BrowseFolder)
button2.grid(column=1, row=1, padx = 22, pady=10)

#predict
#button3 = Button(root, text="Predict", command=predict)
#button3.grid(column=0, row=4, padx = 0, pady=10)

#clearbox
button3 = Button(root, text="Clear Text Box", command=clear)
button3.grid(column=2, row=6)

#exit
button3 = Button(root, text="Close Window", command=close_window)
button3.grid(column=2, row=7)

txt = scrolledtext.ScrolledText(root, width=40, height=10)
txt.grid(column=0, row=6, padx = 22, pady=10)

root.mainloop()
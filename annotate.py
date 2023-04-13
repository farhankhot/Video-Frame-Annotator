from tkinter import *
from PIL import ImageTk, Image
import os
import natsort

root = Tk()
root.geometry("700x700")
root.focus_set()

initial_tracklets_dir = ""
master_list = []
current_image_in_folder_index = 0
current_snmot_index=0
current_folder_index=0
master_list_txt_file_dir = "" 

snmot_list=[]
def create_snmot_list():
  for snmot in os.listdir(initial_tracklets_dir):
    snmot_list.append(snmot)
create_snmot_list()

folder_list=[]
def folder_list_in_a_snmot(current_snmot_index):
  folder_list.clear()
  snmot_name = snmot_list[current_snmot_index]
  for folder_no in os.listdir(initial_tracklets_dir+'/'+snmot_name):
    folder_list.append(folder_no)

def images_in_a_folder_of_a_snmot(current_folder_index, current_snmot_index):
  master_list.clear()
  snmot_name = snmot_list[current_snmot_index]
  folder_name = folder_list[current_folder_index]
  for folder_no in os.listdir(initial_tracklets_dir+'/'+snmot_name):
    for image in os.listdir(initial_tracklets_dir+'/'+snmot_name+'/'+folder_name):
      temp = ImageTk.PhotoImage(Image.open(initial_tracklets_dir+'/'+snmot_name+'/'+
                                           folder_name+'/'+image))
      master_list.append(temp)
    break

##===== Initialization ========
folder_list_in_a_snmot(0)
print(folder_list)
images_in_a_folder_of_a_snmot(0, 0)
##print(master_list)

label = Label(image=master_list[0])
label.grid(row=1, column=0, columnspan=3)
##===== Initialization ========

def display_img(img_no):
  global label
  label = Label(image=master_list[img_no])
  label.grid(row=1, column=0, columnspan=3)

def image_forward(event):
  global current_image_in_folder_index
    
  label.grid_forget()
  current_image_in_folder_index += 1
  display_img(current_image_in_folder_index)

def folder_forward():
  global current_folder_index
  
  label.grid_forget()
  current_folder_index += 1
  images_in_a_folder_of_a_snmot(current_folder_index, current_snmot_index)
  display_img(0)

def snmot_forward(event):
  global current_snmot_index
  global current_folder_index
  label.grid_forget()

  current_snmot_index += 1
  folder_list_in_a_snmot(current_snmot_index)
  print(folder_list)
  current_folder_index = 0
  images_in_a_folder_of_a_snmot(0, current_snmot_index)
  display_img(0)  

T = Text(root, height = 2, width = 10)

def jersey_entry(event):
  jersey_number = T.get("1.0", "end")
  with open(master_list_txt_file_dir, 'a') as f:
    f.write(jersey_number+"\n")
  T.delete("1.0", "end")

##  if current_snmot_index == len(folder_list):
##    snmot_forward()

  folder_forward()
  
T.grid()
root.bind('<Right>', image_forward)
root.bind('<s>', snmot_forward)
root.bind('<Return>', jersey_entry)

root.mainloop()
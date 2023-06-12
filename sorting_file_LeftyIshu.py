# -*- coding: utf-8 -*-
"""
Created on Fri Nov 1 1:33:11 2022

@author: Lefty Ishu
"""


from tkinter import*
from tkinter import filedialog
import os
import shutil


class sorting_app:
    def __init__(self, window):
        # creating window: Create the GUI application main window.
        self.window = window
        
        # title for window
        self.window.title("File Sorting Web Application || Lefty_Ishu")
        
        # window width in pixel x height in pixel + gap from left + gap from top
        self.window.geometry("1350x700+0+0")
        
        
        title = Label(window, text = "File Sorting Application", font = ("Arial", 40), bg = "#282b2e", fg = "white").place(x = 0, y = 20, relwidth = 1)



        # ====================== section 1 =======================
        self.foldername = StringVar()
        
        # Select folder 
        select_folder = Label(window, text = "Select folder", font = ("times new roman", 25)).place(x = 50, y = 150)
        
        # entry field
        text_folder_name = Entry(window, textvariable = self.foldername ,font = ("times new roman", 25), state = "readonly").place(x = 250, y = 150, width = 500)

        # browse button 
        btn_browse = Button(window, command = self.browse_func, text = "Browse", font = ("times new roman", 25), bg = "#223345", fg = "white", cursor = "hand2").place(x = 800, y = 150, height = 40, width = 150)



        # ====================== section 2 =======================
        
        
        frame = Frame(window, bd = 2, relief = RIDGE, bg = "grey").place(x = 50, y = 250, width = 1250, height = 280)

        extention_support = Label(window, text = "Extentions Support", font = ("times new roman", 20, "bold"), bg = "grey").place(x = 100, y = 280)
        documents = Label(window, text = "Documents:      .pdf, .doc, .docx, .txt, .ppt, .xls, .xlsx, .csv", font = ("times new roman", 15), bg = "grey").place(x = 100, y = 330)
        images = Label(window, text = "Images:            .jpeg, .jpg, .png", font = ("times new roman", 15), bg = "grey").place(x = 100, y = 370)
        videos = Label(window, text = "Videos:            .mp4, .ogg, .mov", font = ("times new roman", 15), bg = "grey").place(x = 100, y = 410)
        audios = Label(window, text = "Audios:            .mp3, .midi", font = ("times new roman", 15), bg = "grey").place(x = 100, y = 450)
        
        
        # ==== Start button ====
        btn_start = Button(window, command = self.start_func, text = "Start", font = ("times new roman", 25), bg = "#223345", fg = "white", cursor = "hand2").place(x = 600, y = 600, height = 40, width = 150)


        # folders and extention dictionary
        self.folders = {
                "documents" : ["pdf", "doc", "docx", "txt", "ppt", "xls", "xlsx", "csv"],
                "images" : ["jpeg", "jpg", "png"],
                "videos" : ["mp4", "ogg", "mov"],
                "audios" : ["mp3", "midi", "mpeg"],
                "coding" : ["py"]        }
 

# function for browse button
    def browse_func(self):
        op = filedialog.askdirectory(title = "Select folder for sorting")
        self.foldername.set(str(op))
        
        self.pickup_path = self.foldername.get()
        self.others = "others"


        # taking all folders/files from pick up path in all_files variable
        self.all_files = os.listdir(self.pickup_path)        
        

# function for create folder (if not exist) and move files according to extention
    def CreateMove(self,extention, file_name):
        for folder_name in self.folders:
            if extention in self.folders[folder_name]:
                if folder_name not in os.listdir(self.pickup_path):
                    os.mkdir(os.path.join(self.pickup_path, folder_name))
                    # os.mkdir(os.path.isfile(drop_path + "\\" + folder_name))
                shutil.move(os.path.join(self.pickup_path, file_name),os.path.join(self.pickup_path, folder_name))
                break
            
        else:
            if self.others not in os.listdir(self.pickup_path):
                os.mkdir(os.path.join(self.pickup_path, self.others))
            shutil.move(os.path.join(self.pickup_path, file_name),os.path.join(self.pickup_path, self.others))

        
# function for start button
    def start_func(self):
        # start checking files one by one in all_files variable, if that is file (not folder) then go for CreateMove function
        for file in self.all_files:
            if os.path.isfile(os.path.join(self.pickup_path, file)) == True:
                self.CreateMove(file.split(".")[-1], file)
            # print(f"Total files: {length} || Move Done: {count} || Left with: {length - count}")
        
        
        
# folder's rename function: If in pick_up path any folder exist then rename that folder(s) in lower case
    def rename(self):
        for folder in os.listdir(self.pickup_path):
            if os.path.isdir(os.path.join(self.pickup_path, folder)) == True:
                os.rename(os.path.join(self.pickup_path, folder), os.path.join(self.pickup_path,folder.lower()))
                
    
# calling rename function, if that folder exist in uppercase or  in capitalize name then this function will rename that folder in lower case
        self.rename() 
        
        
            
            
            
    
            

    
window = Tk()
object = sorting_app(window)





# Enter the main event loop to take action
window.mainloop()


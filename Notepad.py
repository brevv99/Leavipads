import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import Frame

class Notepad:

    #variables
    __root = Tk()
    #AD9893
    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root, bg="#706867",fg="white", font="Courier", cursor="xterm #ffffff")
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisFormatMenu = Menu(__thisMenuBar, tearoff=0)
    __thisViewMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):

        
        #initialization

        #set icon
        try:
        		self.__root.wm_iconbitmap("img/daun.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
        		pass

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("Untitled - Notepad")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="New     ",command=self.__newFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Open      ",command=self.__openFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Save As      ",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit        ",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="  Cut  ",command=self.__cut)
        self.__thisEditMenu.add_separator()
        self.__thisEditMenu.add_command(label="  Copy  ",command=self.__copy)
        self.__thisEditMenu.add_separator()
        self.__thisEditMenu.add_command(label="  Paste  ",command=self.__paste)
        #self.__thisEditMenu.add_separator()
        self.__thisMenuBar.add_cascade(label="  Edit  ",menu=self.__thisEditMenu)

        self.__thisFormatMenu.add_command(label="Word Wrap",command=self.__showFormat)
        self.__thisFormatMenu.add_separator()
        self.__thisFormatMenu.add_command(label="Font",command=self.__showFormat)
        #self.__thisFormatMenu.add_separator()
        self.__thisMenuBar.add_cascade(label="Format",menu=self.__thisFormatMenu)


       
        self.__thisViewMenu.add_command(label="Status Bar", state=tkinter.DISABLED)
        self.__thisViewMenu.add_separator()
        self.__thisMenuBar.add_cascade(label="View",menu=self.__thisViewMenu)


        self.__thisHelpMenu.add_command(label="Check For Update",command=self.__showUpdate)
        self.__thisHelpMenu.add_separator()
        self.__thisHelpMenu.add_command(label="About Notepad",command=self.__showAbout)
        self.__thisHelpMenu.add_separator()
        self.__thisHelpMenu.add_command(label="View Help",command=self.__showAboutView)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        exitapp = askokcancel('Exit', "Are You Sure To Exit?")
        if exitapp: 
            self.__root.destroy()
        #exit()

    def __showUpdate(self):
        showinfo("Notepad - Info" ,"No Update Available")

    def __showAbout(self):
        showinfo("Notepad - Info","Notepad Beta Version 1.0.2 Leavi Inc. Copyright By Leavi.")

    def __showAboutView(self):
        showerror("Notepad - Error","You do not have permission to access this menu. Contact your network administrator to request access.")

    #def __showView(self):
        #showwarning("Notepad - Warning", "This Menu Still Develop In Beta Version")

    def __showFormat(self):
        showwarning("Notepad - Warning", "This Menu Has Been Deleted In Beta Version")

    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=650,height=400)
notepad.run()



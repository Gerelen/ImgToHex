from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import os, glob

class Window():

	def __init__(self, root):
		self.root = root
		self.menu = Menu(root)
		root.config(menu=self.menu)

	def ImageToBMP(self,file1,file2):
		#Upload Image and save as BMP
		self.img_hex = Image.open(file1)
		self.img_hex.save(file2)

	def window_menu(self):
		self.file = Menu(self.menu)
		self.file.add_command(label='Upload Image', command=self.upload_image)
		self.file.add_command(label='Convert To Hex')
		self.menu.add_cascade(label='File', menu=self.file)

	def hex_window(self):
		self.root.title('Window')
		self.root.resizable(width=False,height=False)
		self.window_menu()
		
		return self.root

	def upload_image(self):
		self.image_file = askopenfilename(initialdir = "/", title = "Select File", filetypes = (('png files', "*.png"), ("All Files", "*.*")))
		for k in glob.glob(self.image_file):
			self.i = PIL.Image.open(k)
			self.i = self.i.resize((255,255))
		self.render = ImageTk.PhotoImage(image=self.i)
		self.img = Label(root, image=self.render)
		self.img.image = self.render
		self.img.place(x=0,y=0)

root = Tk()
root.geometry('510x510')
app = Window(root)
app.hex_window()
root.mainloop()

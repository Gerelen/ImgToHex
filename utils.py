from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import os, glob

class Window():

	def __init__(self, root):
		self.return_if = False
		self.root = root
		self.menu = Menu(root)
		root.config(menu=self.menu)
		self.ImSet = ImageSetup()

	def window_menu(self):
		self.file = Menu(self.menu)
		self.file.add_command(label='Upload Image', command=self.upload_image)
		self.file.add_command(label='Resize 255?', command=self.return_if_statetements)
		self.file.add_command(label='Convert To Hex', command=self.ImSet.BMP2Img)
		self.menu.add_cascade(label='File', menu=self.file)

	def hex_window(self):
		self.root.title('Window')
		self.root.resizable(width=False,height=False)
		self.window_menu()
		
		return self.root

	def return_if_statetements(self):
		#Add later method to turn on and off
		self.return_if =  True
		print('Return set to {}'.format(self.return_if))
		return self.return_if

	def upload_image(self):
		self.image_file = askopenfilename(initialdir = "/", title = "Select File", filetypes = (('png files', "*.png"), ("All Files", "*.*")))
		for k in glob.glob(self.image_file):
			self.i = PIL.Image.open(k)
			width, height = self.i.size

		if height >= width and self.return_if == True:
			if height > 255:
				self.i = self.ImSet.resize_height_scalar(self.i)
		if width > height and self.return_if == True:
			if width > 255:
				self.i = self.ImSet.resize_width_scalar(self.i)

		self.render = ImageTk.PhotoImage(image=self.i)
		self.img = Label(root, image=self.render)
		self.img.image = self.render
		self.img.place(x=0,y=0)

class ImageSetup():

	def resize_height_scalar(self, image_h_resize):
		self.baseheight = 255
		#width,height = img.size()
		self.image_h_resize = image_h_resize
		self.hpercent = (self.baseheight/float(self.image_h_resize.size[1]))
		self.wsize = int((float(self.image_h_resize.size[0])*float(self.hpercent)))
		self.image_h_resize = self.image_h_resize.resize((self.wsize,self.baseheight), PIL.Image.ANTIALIAS)

		return self.image_h_resize

	def resize_width_scalar(self, image_w_resize):
		self.basewidth = 255
		self.image_w_resize = image_w_resize
		self.wpercent = (self.basewidth/float(self.image_w_resize.size[0]))
		self.hsize = int((float(self.image_w_resize.size[1])*float(self.wpercent)))
		self.image_w_resize = self.image_w_resize.resize((self.basewidth, self.hsize), PIL.Image.ANTIALIAS)

		return self.image_w_resize

	def ImageToBMP(self,file1,file2):
		#Upload Image and save as BMP
		#Switch red and blue colors
		#Rotate 180
		#Flip Horizontally
		self.img_hex = PIL.Image.open(file1)
		self.img_hex.save('image.bmp')

	def BMP2Img(self, bmp_image):



root = Tk()
root.geometry('260x260')
app = Window(root)
app.hex_window()
root.mainloop()

"""
TODO LIST:

Delete old image when creating new image
Move image over in window
Make return_if_statements a switch
"""

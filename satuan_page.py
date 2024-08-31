from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from configure import Config



class Satuan_Window(Tk):
	def __init__(self,App):
		self.app = App
		self.config = self.app.config
		self.titles = 'Satuan maker'
		self.width = self.app.width
		self.height = self.app.height
		self.screen = self.app.screen

		super().__init__()

		self.geometry(self.screen)
		self.title(self.titles)
		self.resizable(0,0)
		

		self.create_container()
		self.pages = {}
		self.Create_main_pages()

	def create_container(self):
		self.container = Frame(self)
		self.container.pack(fill="both", expand=True)

	def Create_main_pages(self):
		self.pages['Main_Page'] = Page(self.app,self.container)

class Satuan_Page(Frame):
	def __init__(self) :

		base = 30
		ratio = (8, 6)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+350+100"

	
		self.config = Config()
		self.window = Satuan_Window(self)


			
	#def run(self):
		#self.window.mainloop()

	def quit(self):
		tk.Tk.destroy(self.window)

class Page(Frame):
	def __init__(self,App,Parent):
		self.app = App
		self.settings = App.config
		
		super().__init__(Parent)

		self.configure(bg='white')
		
		self.satuan=None

		self.grid(row=0, column=0, sticky="nsew")

		Parent.grid_rowconfigure(0, weight=1)
		Parent.grid_columnconfigure(0, weight=1)

		self.Main_Pages()

	def Del_Satuan(self):
		if self.satuan.get() in self.settings.satuan:
			choose = msg.askyesnocancel('Confirmation','Are You Sure To Delete This Satuan')
			if choose :
				del self.settings.satuan[self.settings.satuan.index(self.satuan.get())]
				self.settings.Write_Data(self.settings.data_satuan,self.settings.satuan)
				self.app.quit()



			elif choose == False:
				self.app.quit()

			else:
				pass
		else:
			msg.Message(f'There are no satuan that call {self.satuan.get()}')
			msg.showinfo('Error',f'There are no satuan that call {self.satuan.get()}')



	def Add_Satuan(self):
		self.old_Satuan_List = self.settings.satuan
		self.satuan_list = []
		for all_object in self.old_Satuan_List:
			self.satuan_list.append(all_object.lower())
		
	
		if self.satuan.get().lower() in self.satuan_list:
			choose = msg.askyesnocancel('Confirmation','There Are An Similiar Satuan In Your Last Data \n            Are You Sure Want to Save This')
			if choose:
				self.settings.satuan.append(self.satuan.get())
				self.settings.Write_Data(self.settings.data_satuan,self.settings.satuan)
				self.app.quit()

				
			elif choose == False:
				self.app.quit()
			else:
				pass

		else:
			choose = msg.askyesnocancel('Confirmation','Are You Sure Want To Save This')
			if choose:
				self.settings.satuan.append(self.satuan.get())
				self.settings.Write_Data(self.settings.data_satuan,self.settings.satuan)
				self.app.quit()
				
			elif choose == False:
				self.app.quit()

			else:
				pass

	def choose_buttom(self,arg):
		frame_h = self.app.height
		frame_w = self.app.width

		if self.satuan !=None:
			self.satuan.destroy()

		
		if arg =='add':
			
			self.Main_Frame = tk.Frame(self,width=frame_w,height=2*frame_h//3,bg='white')
			self.Main_Frame.grid(column=0,row=1)

			
			self.Label = tk.Label(self.Main_Frame,text='Input Satuan in here',bg='white')
			self.Label.grid(column=0,row=0,sticky='w')

			self.satuan = tk.Entry(self.Main_Frame,bg='white',bd=1)
			self.satuan.grid(column=1,row=0,sticky='e')

			self.command= self.Add_Satuan

		else:
			self.Main_Frame = tk.Frame(self,width=frame_w,height=2*frame_h//3,bg='white')
			self.Main_Frame.grid(column=0,row=1)

			self.Label = tk.Label(self.Main_Frame,text='Choose Satuan',bg='white')
			self.Label.grid(column=0,row=0,sticky='w')

			self.satuan = ttk.Combobox(self.Main_Frame,value=self.app.config.satuan)
			self.satuan.grid(column=1,row=0,sticky='e')

			self.command = self.Del_Satuan

		self.Button = tk.Button(self.Main_Frame,text='Press the Button',command=self.command)
		self.Button.grid(column=0,row=1,columnspan=2)




	def Main_Pages(self):
		frame_h = self.app.height
		frame_w = self.app.width 

		self.Radio_bottom_frame = tk.Frame(self,width = frame_w,height=frame_h//3)
		self.Radio_bottom_frame.grid(column=0,row=0)

		self.Radio_delete_choose_bottom = tk.Radiobutton(self.Radio_bottom_frame,text='delete',font=('arial',12),bd=0,bg='white',command = lambda:self.choose_buttom('delete'))
		self.Radio_delete_choose_bottom.grid(row=0,column=0,ipadx=25)

		self.Radio_add_choose_bottom = tk.Radiobutton(self.Radio_bottom_frame,text='add',font=('arial',12),bd=0,bg='white',command = lambda:self.choose_buttom('add'))
		self.Radio_add_choose_bottom.grid(row=0,column=1,ipadx=25)









if __name__ == '__main__':
	Page = Satuan_Page()
	#Page.run()
	
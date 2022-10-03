import tkinter as tk
import random
def method_name():
	import easygui
	return easygui

easygui = method_name()


stu_list=['stu1','stu2','stu3','stu4','stu5','stu6',
		  'stu7','stu8','stu9','stu10','stu11',
		  'stu12','stu13','stu41','stu15',]

root = tk.Tk()
root.geometry("720x720")

key=easygui.passwordbox(msg='Enter your password.')


root.mainloop()

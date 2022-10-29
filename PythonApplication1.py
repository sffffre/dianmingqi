import tkinter as tk
import random

stu_list = ['stu1','stu2','stu3','stu4','stu5','stu6',
	'stu7','stu8','stu9','stu10','stu11',
	'stu12','stu13','stu14','stu15',
               'stu16','stu17','stu18','stu19','stu20','stu21',
	'stu23','stu24','stu25','stu26','stu27',
	'stu28','stu29','stu30','stu31',
	'stu32','stu33','stu34','stu35',
               'stu36','stu37','stu38','stu39','stu40','stu41',
	'stu42','stu43','stu44','stu45','stu46',
	'stu47','stu48','stu49','stu50']

stu = '开始点名'
last = []

root = tk.Tk()
root.geometry("900x900")
root.title('点名器')
root.resizable(False,False)



label = tk.Label(win, text=stu,font=('宋体',20, 'bold italic'),width=30,height=5,)
root.mainloop()

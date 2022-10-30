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
re_list = []
new_list = []


root = tk.Tk()
root.geometry("900x900")
root.title('点名器')
root.resizable(False,False)

stu = '开始点名'
last = []
text = tk.StringVar()
text.set(stu)

label = tk.Label(root, text=stu,font=('黑体',35),width=30,height=5,textvariable=text)
label.place(x=150,y=300)

def callback():
    while True:
        stu=random.choice(stu_list)
        if stu in re_list:
            pass
        else:
            re_list.append(stu)
            if len(re_list) > 5:
                del re_list[0]
            break
    
    text.set(stu)

b = tk.Button(root, text="点名", command=callback, width=20,height=10)
b.place(x=300,y=750)

root.mainloop()

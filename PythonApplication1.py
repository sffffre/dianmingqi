import tkinter as tk
import random

stu_list = ['龚泉全','李知衡','李坤泽','蒲俊翔','刘芮含','秦子恒',
	'戴吉满','彭康峻','郭隆浩','杨曜恺','代淳玺',
	'亢泓博','龚子涵','李忻芸','张芮博',
               '张家洲','丁翌航','唐粲然','张齐家','蔡述合',
            '肖知止','彭诗涵','杨睿杰','刘知几','殷梦可',
            '曾煜航','李君昊','吴思诺','乔瞰','陈禹竹',
	'杜瀚霖','杜芋霏','刘衍辰','杨沛翰','张森越','覃索菲',
            '杨沁妤','刘泫妙','赵思齐','李秉战',
	'黄婉榕','卢彦朵','郑绍益','邓钦元','邓涵',
	'魏梓涵','朱美霖','楚言熙','张翰予','龚泉全','龚泉全','龚泉全',]
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

label = tk.Label(root, text=stu,font=('黑体',60),width=20,height=5,textvariable=text)
label.place(x=0,y=50)

def callback():
    while True:
        stu=random.choice(stu_list)
        if stu in re_list:
            pass
        else:
            re_list.append(stu)
            if len(re_list) > 7:
                del re_list[0]
            break
    
    text.set(stu)

b = tk.Button(root, text="点名", command=callback, width=20,height=10)
b.place(x=300,y=550)

root.mainloop()

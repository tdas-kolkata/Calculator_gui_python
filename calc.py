from tkinter import *
from tkinter.font import Font

root=Tk()
root.configure(bg='steel blue')


a=' '
equation=StringVar()

calculation=Label(root,textvariable=equation,bd=10,relief=SUNKEN,width=27,
                    font=Font(family='arial',size='30',weight='bold'))
equation.set(' ')
calculation.grid(columnspan=5,sticky=E,padx=6,pady=4)


def btp(num):
    global a
    a=a+str(num)
    equation.set(a)

def eqp():
    global a
    total=str(eval(a))
    a=total
    equation.set(a)
    
def clr():
    global a
    a=''
    equation.set(a)

def delete():
    global a
    a=a[:-1]
    equation.set(a)

b7=Button(root,text='    7    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(7))
b7.grid(row=1,column=0,padx=8,pady=5)
b8=Button(root,text='    8    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(8))
b8.grid(row=1,column=1,padx=8,pady=5)
b9=Button(root,text='    9    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(9))
b9.grid(row=1,column=2,padx=8,pady=5)
b4=Button(root,text='    4    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(4))
b4.grid(row=2,column=0,padx=8,pady=5)
b5=Button(root,text='    5    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(5))
b5.grid(row=2,column=1,padx=8,pady=5)
b6=Button(root,text='    6    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(6))
b6.grid(row=2,column=2,padx=8,pady=5)
b1=Button(root,text='    1    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(1))
b1.grid(row=3,column=0,padx=8,pady=5)
b2=Button(root,text='    2    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(2))
b2.grid(row=3,column=1,padx=8,pady=5)
b3=Button(root,text='    3    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(3))
b3.grid(row=3,column=2,padx=8,pady=5)
b0=Button(root,text='    0    ',
          font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(0))
b0.grid(row=4,column=1,padx=8,pady=5)




plus=Button(root,text='    +    ',
            font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp('+'))
plus.grid(row=1,column=3,padx=8,pady=5)
minus=Button(root,text='    -    ',
             font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp('-'))
minus.grid(row=2,column=3,padx=8,pady=5)
multiply=Button(root,text='    x    ',
                font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp('*'))
multiply.grid(row=3,column=3,padx=8,pady=5)
devide=Button(root,text='    /    ',
              font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp('/'))
devide.grid(row=4,column=3,padx=8,pady=5)
equal=Button(root,text='    =    ',
             font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='orange',fg='white',bd=5,command=eqp)
equal.grid(row=4,column=2,padx=8,pady=5)
dot=Button(root,text='    .    ',
           font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp('.'))
dot.grid(row=4,column=4,padx=8,pady=5)

clear=Button(root,text='    C    ',
             font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='red',fg='white',bd=5,command=clr)
clear.grid(row=4,column=0,padx=8,pady=5)
delete=Button(root,text='  DEL  ',
             font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='indian red',fg='white',bd=5,command=delete)
delete.grid(row=1,column=4,padx=8,pady=5)
br1=Button(root,text='    (    ',
             font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp('('))
br1.grid(row=2,column=4,padx=8,pady=5)
br2=Button(root,text='    )    ',
             font=Font(family='arial',size='20',weight='bold'),relief=RAISED,bg='black',fg='white',bd=5,command=lambda:btp(')'))
br2.grid(row=3,column=4,padx=8,pady=5)





root.mainloop()

from tkinter import*
import random
import time
import datetime
import tkinter.messagebox


new=Tk()
new.title('menu')
new.geometry("1350x750+0+0")
new.configure(background='#E2CCA3')

frame=Frame(new,bg='#E2CCA3',bd=10,pady=10,padx=10,relief=RIDGE)
frame.pack(side=TOP)
lbltitle=Label(frame,font=('arial',40,'bold'),text="MENU",bd=10,bg='#E2CCA3',fg='#423930')
lbltitle.grid(row=0,column=0)

menuframe=Frame(new,bg='#E2CCA3',bd=20,width=1200,height=600,relief=RIDGE)
menuframe.pack()

drinksframe=Frame(menuframe,bg='#E2CCA3',bd=10,width=600,height=500,relief=RIDGE)
drinksframe.pack(side=LEFT)
hotdrinksframe=Frame(drinksframe,bg='#E2CCA3',bd=10,width=300,height=200,relief=RIDGE)
hotdrinksframe.pack(side=TOP)
lbl1title=Label(hotdrinksframe,font=('arial',20,'bold'),text="HOT DRINKS",bd=20,bg='#E2CCA3',fg='#423930')
lbl1title.grid(row=0,column=0)
colddrinksframe=Frame(drinksframe,bg='#E2CCA3',bd=10,width=300,height=200,relief=RIDGE)
colddrinksframe.pack(side=BOTTOM)
lbl2title=Label(colddrinksframe,font=('arial',19,'bold'),text="COLD DRINKS",bd=20,bg='#E2CCA3',fg='#423930')
lbl2title.grid(row=0,column=0)

foodsframe=Frame(menuframe,bg='#E2CCA3',bd=10,width=600,height=500,relief=RIDGE)
foodsframe.pack(side=RIGHT)
lbl3title=Label(foodsframe,font=('arial',19,'bold'),text="SNACKS",bd=20,bg='#E2CCA3',fg='#423930')
lbl3title.grid(row=0,column=0)
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()

#checkbutton for drinks
latte=Checkbutton(hotdrinksframe,text='Latte',variable=var1,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=1,sticky=W)
americano=Checkbutton(hotdrinksframe,text='Americano',variable=var2,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=2,sticky=W)
espresso=Checkbutton(hotdrinksframe,text='Espresso',variable=var3,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=3,sticky=W)
cappuccino=Checkbutton(hotdrinksframe,text='Cappuccino',variable=var4,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=4,sticky=W)
hotchocolate=Checkbutton(hotdrinksframe,text='hotchocolate',variable=var5,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=5,sticky=W)


coke=Checkbutton(colddrinksframe,text='coke',variable=var6,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=1,sticky=W)
fanta=Checkbutton(colddrinksframe,text='fanta',variable=var7,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=2,sticky=W)
sprite=Checkbutton(colddrinksframe,text='sprite',variable=var8,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=3,sticky=W)
pepsi=Checkbutton(colddrinksframe,text='pepsi',variable=var9,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=4,sticky=W)
dew=Checkbutton(colddrinksframe,text='dew',variable=var10,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=5,sticky=W)

txtlatte=Entry(hotdrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtlatte.grid(row=1,column=1)
txtamericano=Entry(hotdrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtamericano.grid(row=2,column=1)
txtexpresso=Entry(hotdrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtexpresso.grid(row=3,column=1)
txtcappuccino=Entry(hotdrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtcappuccino.grid(row=4,column=1)
txthotchocolate=Entry(hotdrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txthotchocolate.grid(row=5,column=1)

txtcoke=Entry(colddrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtcoke.grid(row=1,column=1)

txtfanta=Entry(colddrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtfanta.grid(row=2,column=1)

txtsprite=Entry(colddrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtsprite.grid(row=3,column=1)

txtpepsi=Entry(colddrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtpepsi.grid(row=4,column=1)

txtdew=Entry(colddrinksframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtdew.grid(row=5,column=1)



#check button for foods
momo=Checkbutton(foodsframe,text='momo',variable=var11,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=1,sticky=W)
chowmein=Checkbutton(foodsframe,text='chowmein',variable=var12,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=2,sticky=W)
thukpa=Checkbutton(foodsframe,text='thukpa',variable=var13,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=3,sticky=W)
pizza=Checkbutton(foodsframe,text='pizza',variable=var14,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=4,sticky=W)
burger=Checkbutton(foodsframe,text='Burger',variable=var15,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=5,sticky=W)
chicken_chilly=Checkbutton(foodsframe,text='Chicken chilly',variable=var16,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=6,sticky=W)
frenchfries=Checkbutton(foodsframe,text='Fries',variable=var17,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=7,sticky=W)
pasta=Checkbutton(foodsframe,text='Pasta',variable=var18,onvalue=1,offvalue=0,font=('arial',15,'bold'),bg='#E2CCA3').grid(row=8,sticky=W)

txtmomo=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtmomo.grid(row=1,column=1)
txtchowmein=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtchowmein.grid(row=2,column=1)
txtthukpa=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtthukpa.grid(row=3,column=1)
txtpizza=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtpizza.grid(row=4,column=1)
txtburger=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtburger.grid(row=5,column=1)
txtchicken_chilly=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtchicken_chilly.grid(row=6,column=1)
txtfrenchfries=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtfrenchfries.grid(row=7,column=1)
txtpasta=Entry(foodsframe,font=('arial',11,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED)
txtpasta.grid(row=8,column=1)


new.mainloop()


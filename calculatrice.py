
from  tkinter import *
root=Tk()
root.title("Calculatrice")
root.geometry("400x550")
# root.config(bg="#456789")

#La valeur 1
lab1=Label(root,text="valeur 1:",bg="yellow",fg="blue")
lab1.place(x=25,y=25)
val1=Entry(root,bg="pink")
val1.place(x=110,y=25)
#La valeur 2
lab2=Label(root,text="valeur 2:",bg="yellow" ,fg="blue")
lab2.place(x=25,y=50)
val2=Entry(root,bg="pink")
val2.place(x=110,y=50) 
#Creat LabelFreameS
labelframe  = LabelFrame(root, text="opération",fg="black", padx=15, pady=15)
labelframe.place(x=10,y=140)
#Espace d'Affichage
lab3=Label(root,text=" "*40,bg="yellow" ,fg="blue",padx=70)
lab3.place(x=100,y=160)
#Les fonctions
def plus():
    try:
        x=float(val1.get())
        y=float(val2.get())
        z=x+y
        lab3["text"]="{} + {} = {}".format(x,y,z)
    except:
        lab3["text"]="Veuillez saisir les valeurs !"
def sus():
    try:
        x=float(val1.get())
        y=float(val2.get())
        z=x-y
        lab3["text"]="{} - {} = {}".format(x,y,z)
    except:
        lab3["text"]="Veuillez saisir les valeurs !"
def mul():
    try:
        x=float(val1.get())
        y=float(val2.get())
        z=x*y
        lab3["text"]="{} * {} = {}".format(x,y,z)
    except:
        lab3["text"]="Veuillez saisir les valeurs !"
def div():
    try:
        x=float(val1.get())
        y=float(val2.get())
        z=x/y
        lab3["text"]="{} / {} = {}".format(x,y,z)
    except:
        lab3["text"]="Veuillez saisir les valeurs !" 
def dive():
    try:
        x=float(val1.get())
        y=float(val2.get())
        z=x//y
        lab3["text"]="{} // {} = {}".format(x,y,z)
    except:
        lab3["text"]="Veuillez saisir les valeurs !"         

def effacer():
    val1.delete(0,END)
    val2.delete(0,END)
    lab3["text"]=" "*40

a =IntVar()
op1 = Radiobutton(labelframe, text="+", variable=a, value="1", command=plus)
op1.pack(anchor = W)

op2 = Radiobutton(labelframe, text="-", variable=a, value="2", command=sus)
op2.pack(anchor = W)

op3 = Radiobutton(labelframe, text="*", variable=a, value="3", command=mul)
op3.pack(anchor = W)

op4 = Radiobutton(labelframe, text="/", variable=a, value="4", command=div)
op4.pack(anchor = W)

op5 = Radiobutton(labelframe, text="//", variable=a, value="5", command=dive)
op5.pack(anchor = W)

op6 = Radiobutton(labelframe, text="CE", variable=a, value="6", command=effacer)
op6.pack(anchor = W)








# labelframe = LabelFrame(root,text="opérqtion")
# labelframe.pack(fill="both", expand="yes")  
# val2=Entry(labelframe,bg="pink")
# val2.grid(row='5',column='1')






#run
root.mainloop()

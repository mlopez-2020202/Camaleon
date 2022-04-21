import tkinter
import random

index = tkinter.Tk()
index.title('background camaleón')
index.geometry('1000x600')
#Funciones
colors = ['red', 'blue', 'pink', 'green', 'yellow', 'orange','brown', 'violet', 'light blue', 'silver']
def changeColor():
    randomColor = random.choice(colors)
    index.config(background = randomColor)
    lblcolor['text'] = text='Background color: ' + randomColor 
#interfaz
btnCambio = tkinter.Button(index, text='Change', bg='black', fg='White', font='Century 15', width=15, height=3, command=changeColor)
btnCambio.place(x=400, y=400)
lblcolor = tkinter.Label(index, text='Backgroud color:', bg='black', fg='white',font='Century 10', width=30, height=3)
lblcolor.place(x=380, y=100)

index.mainloop()
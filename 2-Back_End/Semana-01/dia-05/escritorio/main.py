from tkinter import *

class Computadora:



  def __init__(self,app):
    self.app = app
    self.app.title('Inventario de Computadoras')

    # Frame
    frame = LabelFrame(self.app, text='computadora')
    frame.grid(row=0, column=0, columnspan=3,pady=10)

    # Componentes del Formulario
    lbSistema = Label(frame,text='SISTEMA OPERATIVO')
    lbSistema.grid(row=1,column=0)
    self.txtSistema = Entry(frame)
    self.txtSistema.grid(row=2,column=0)

app = Tk() #Se instancia el Tk hacia app
appComputadora = Computadora(app)
app.mainloop()
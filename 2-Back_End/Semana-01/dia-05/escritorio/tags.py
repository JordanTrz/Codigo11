import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=332
        height=499
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "Sistema Operativo: "
        GLabel_551.place(x=40,y=40,width=108,height=30)

        GLineEdit_555=tk.Entry(root)
        GLineEdit_555["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_555["font"] = ft
        GLineEdit_555["fg"] = "#333333"
        GLineEdit_555["justify"] = "center"
        GLineEdit_555["text"] = "Entry1"
        GLineEdit_555.place(x=180,y=40,width=110,height=30)

        GLabel_967=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_967["font"] = ft
        GLabel_967["fg"] = "#333333"
        GLabel_967["justify"] = "center"
        GLabel_967["text"] = "Procesador"
        GLabel_967.place(x=40,y=90,width=70,height=25)

        GLineEdit_810=tk.Entry(root)
        GLineEdit_810["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_810["font"] = ft
        GLineEdit_810["fg"] = "#333333"
        GLineEdit_810["justify"] = "center"
        GLineEdit_810["text"] = "Entry2"
        GLineEdit_810.place(x=180,y=90,width=111,height=30)

        GLabel_275=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_275["font"] = ft
        GLabel_275["fg"] = "#333333"
        GLabel_275["justify"] = "center"
        GLabel_275["text"] = "Memoria Ram"
        GLabel_275.place(x=40,y=140,width=81,height=30)

        GLineEdit_808=tk.Entry(root)
        GLineEdit_808["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_808["font"] = ft
        GLineEdit_808["fg"] = "#333333"
        GLineEdit_808["justify"] = "center"
        GLineEdit_808["text"] = "Entry3"
        GLineEdit_808.place(x=180,y=140,width=111,height=30)

        GButton_883=tk.Button(root)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#5fb878"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Guardar"
        GButton_883.place(x=130,y=220,width=70,height=25)
        GButton_883["command"] = self.GButton_883_command

    def GButton_883_command(self):
        sqlInsertar = "insert into computadoras(sistema,procesador,memoria) values(%,%,%)"
        parametros = (self.nombre.get(),self.email.get())
        self.ejecutarSql(sqlInsertarAlumno,parametros)
        messagebox.showinfo("Registro Exitoso",

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host = "blpznx8pd1lm5icpif6k-mysql.services.clever-cloud.com",
  user = "u50cl7emwy8nc9f2",
  password = "f7K8Ae6bST9vR9O1SRwW",
  database = "blpznx8pd1lm5icpif6k"
)

class App:

    def ejecutarSql(self,sql,parametros = ()):
          mycursor = mydb.cursor()
          mycursor.execute(sql,parametros)
          mydb.commit()

    def Button_command(self):
        sqlInsertar = "insert into registro(nombres,apellidos,planta,day,month,year,hour,minute) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        parametros = (self.nombres.get(),self.apellidos.get(),self.planta.get(),self.day,self.month,self.year,self.hour,self.minute)
        self.ejecutarSql(sqlInsertar,parametros)
        messagebox.showinfo("Registro Exitoso", "Nombres registrados con Exito")

    def __init__(self,root):
      now = datetime.now()
      self.day = now.day
      self.month = now.month
      self.year = now.year
      self.hora = str(now.hour) + ":" + str(now.minute)
      self.hour = now.hour
      self.minute = now.minute


      OUTPUT_PATH = Path(__file__).parent
      ASSETS_PATH = OUTPUT_PATH / Path("./assets")

      def relative_to_assets(path: str) -> Path:
          return ASSETS_PATH / Path(path)

      root.geometry("600x350")
      root.configure(bg = "#FFFFFF")

      canvas = Canvas(
          root,
          bg = "#FFFFFF",
          height = 350,
          width = 600,
          bd = 0,
          highlightthickness = 0,
          relief = "ridge"
      )

      canvas.place(x = 0, y = 0)
      canvas.create_rectangle(
          0.0,
          0.0,
          600.0,
          350.0,
          fill="#003566",
          outline="")

      canvas.create_rectangle(
          299.9999999999999,
          0.0,
          599.9999999999999,
          350.0,
          fill="#FFD60A",
          outline="")

      canvas.create_text(
          327.9999999999999,
          236.0,
          anchor="nw",
          text="Planta",
          fill="#000000",
          font=("Nunito Regular", 13 * -1)
      )

      canvas.create_text(
          327.9999999999999,
          175.0,
          anchor="nw",
          text="Apellidos",
          fill="#000000",
          font=("Nunito Regular", 13 * -1)
      )

      canvas.create_text(
          29.999999999999886,
          81.0,
          anchor="nw",
          text="Control de asistencia",
          fill="#FFFFFF",
          font=("Nunito Bold", 24 * -1)
      )

      canvas.create_text(
          72.99999999999989,
          127.0,
          anchor="nw",
          text="Favor de ingresar sus datos",
          fill="#FFFFFF",
          font=("Nunito Light", 13 * -1)
      )

      image_image_1 = PhotoImage(
          file=relative_to_assets("image_1.png"))
      image_1 = canvas.create_image(
          150.9999999999999,
          229.0,
          image=image_image_1
      )

      canvas.create_text(
          327.9999999999999,
          114.0,
          anchor="nw",
          text="Nombres",
          fill="#000000",
          font=("Nunito Regular", 13 * -1)
      )

      canvas.create_text(
          394.9999999999999,
          40.0,
          anchor="nw",
          text="Mes",
          fill="#000000",
          font=("Nunito Bold", 13 * -1)
      )

      canvas.create_text(
          454.9999999999999,
          40.0,
          anchor="nw",
          text="Año",
          fill="#000000",
          font=("Nunito Bold", 13 * -1)
      )

      canvas.create_text(
          524.9999999999999,
          40.0,
          anchor="nw",
          text="Hora",
          fill="#000000",
          font=("Nunito Bold", 13 * -1)
      )

      canvas.create_text(
          337.9999999999999,
          40.0,
          anchor="nw",
          text="Día",
          fill="#000000",
          font=("Nunito Bold", 13 * -1)
      )

      entry_image_1 = PhotoImage(
          file=relative_to_assets("entry_1.png"))
      entry_bg_1 = canvas.create_image(
          449.9999999999999,
          147.0,
          image=entry_image_1
      )
      entry_1 = Entry(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_1.place(
          x=332.9999999999999,
          y=132.0,
          width=234.0,
          height=28.0
      )

      entry_image_2 = PhotoImage(
          file=relative_to_assets("entry_2.png"))
      entry_bg_2 = canvas.create_image(
          467.4999999999999,
          76.0,
          image=entry_image_2
      )
      entry_2 = Text(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_2.insert('1.0',self.year)
      entry_2.place(
          x=451.9999999999999,
          y=61.0,
          width=34.0,
          height=28.0
      )

      entry_image_3 = PhotoImage(
          file=relative_to_assets("entry_3.png"))
      entry_bg_3 = canvas.create_image(
          539.4999999999999,
          76.0,
          image=entry_image_3
      )
      entry_3 = Text(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_3.insert('1.0',self.hora)
      entry_3.place(
          x=511.9999999999999,
          y=61.0,
          width=55.0,
          height=28.0
      )

      entry_image_4 = PhotoImage(
          file=relative_to_assets("entry_4.png"))
      entry_bg_4 = canvas.create_image(
          407.4999999999999,
          76.0,
          image=entry_image_4
      )
      entry_4 = Text(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_4.insert('1.0',self.month)
      entry_4.place(
          x=391.9999999999999,
          y=61.0,
          width=31.0,
          height=28.0
      )

      entry_image_5 = PhotoImage(
          file=relative_to_assets("entry_5.png"))
      entry_bg_5 = canvas.create_image(
          348.4999999999999,
          76.0,
          image=entry_image_5
      )
      entry_5 = Text(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_5.insert('1.0',self.day)
      entry_5.place(
          x=332.9999999999999,
          y=61.0,
          width=31.0,
          height=28.0
      )

      entry_image_6 = PhotoImage(
          file=relative_to_assets("entry_6.png"))
      entry_bg_6 = canvas.create_image(
          449.9999999999999,
          208.0,
          image=entry_image_6
      )
      entry_6 = Entry(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_6.place(
          x=332.9999999999999,
          y=193.0,
          width=234.0,
          height=28.0
      )

      entry_image_7 = PhotoImage(
          file=relative_to_assets("entry_7.png"))
      entry_bg_7 = canvas.create_image(
          449.9999999999999,
          269.0,
          image=entry_image_7
      )
      entry_7 = Entry(
          bd=0,
          bg="#FFFFFF",
          highlightthickness=0
      )
      entry_7.place(
          x=332.9999999999999,
          y=254.0,
          width=234.0,
          height=28.0
      )

      button_image_1 = PhotoImage(
          file=relative_to_assets("button_1.png"))
      button_1 = Button(
          image=button_image_1,
          borderwidth=0,
          highlightthickness=0,
          command = self.Button_command,
          relief="flat"
      )
      button_1.place(
          x=412.9999999999999,
          y=303.0,
          width=72.0,
          height=24.0
      )

      self.nombres = entry_1
      self.apellidos = entry_6
      self.planta = entry_7

      # window.resizable(False, False)
      # windows.mainloop()
      root.resizable(False, False)
      root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = App(root)

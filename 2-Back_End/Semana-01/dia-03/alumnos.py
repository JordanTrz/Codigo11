# PROGRAMA PARA CRUD DE ALUMNOS
import tabulate

opcion = 0
alumnos = [{'nombre':'cesar','email':'cesarmayta@gmail.com','celular':'999600566'}]

# Funciones
def updateAlumno(alumnos,newOption):
  a = input("Ingrese el " + newOption + "que desea modificar: ")
  for alumno in alumnos:
        if(alumno[newOption] == a):
          getOption = input("Ingrese nuevo el nuevo " + newOption + " a modificar: ")
          alumno[newOption] = getOption

def deleteAlumno(alumnos,newOption):
  a=input("Ingrese el alumno que desea eliminar: ")
  for i,alumno in enumerate(alumnos):
    if(alumno[newOption] == a):
      alumnos.pop(i)

def showAlumnos(alumnos):
  if (len(alumnos) > 0):
    cabeceras = alumnos[0].keys()
    registros = [x.values() for x in alumnos]
    print(tabulate.tabulate(registros,cabeceras))
  else:
    print("NO HAY REGISTROS")


print("==============================")
print("  PROGRAMA DE ALUMNOS CODIGO  ")
print("==============================")
print("MARQUE LA OPCIÓN QUE DESEA EJECUTAR")
print("[1] REGISTRAR ALUMNO")
print("[2] MOSTRAR ALUMNOS")
print("[3] ACTUALIZAR ALUMNO")
print("[4] ELIMINAR ALUMNO")
print("[5] SALIR DEL PROGRAMA")
while(opcion != 5):
      opcion = int(input("INGRESE OPCIÓN: "))
      if(opcion == 1):
            # REGISTRAR ALUMNO
            print("==============================")
            print("   REGISTRO DE NUEVO ALUMNO   ")
            print("==============================")
            nombre = input("Nombre: ")
            email = input("Email: ")
            celular = input("Celular: ")
            dictAlumno = {
              'nombre': nombre,
              'email' : email,
              'celular': celular
            }
            alumnos.append(dictAlumno)
            print("ALUMNO INGRESADO CON ÉXITO!")
      elif(opcion == 2):
            # MOSTRAR ALUMNO
            print("==============================")
            print("       RELACIÓN DE ALUMNOS    ")
            print("==============================")
            # cabeceras = alumnos[0].keys()
            # registros = [x.values() for x in alumnos]
            # print(tabulate.tabulate(registros,cabeceras))
            showAlumnos(alumnos)
      elif(opcion == 3):
            # ACTUALIZAR ALUMNO
            print("==============================")
            print("   ACTUALIZACIÓN DE ALUMNOS   ")
            print("==============================")
            modificar = input("""QUÉ DESEA ACTUALIZAR
                  A: NOMBRE
                  B: EMAIL
                  C: CELULAR
                  """)
            if(modificar == "A"):
              updateAlumno(alumnos, "nombre")
            elif(modificar == "A"):
              updateAlumno(alumnos, "email")
            elif(modificar == "A"):
              updateAlumno(alumnos, "celular")
            else:
              print("Error")
      elif(opcion == 4):
            # ELIMINAR ALUMNO
            print("==============================")
            print("        ELIMINAR ALUMNO       ")
            print("==============================")
            newOption = 'nombre'
            deleteAlumno(alumnos,newOption)
      elif(opcion == 5):
            # SALIR DE PROGRAMA
            print("==============================")
            print(" GRACIAS POR USAR MI PROGRAMA ")
            print("==============================")
            break
      else:
        print("OPCIÓN INVÁLIDA,INGRESE OPCIÓN")

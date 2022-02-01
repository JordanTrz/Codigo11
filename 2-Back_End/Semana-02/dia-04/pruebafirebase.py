import pyrebase

config = {
  "apiKey": "AIzaSyBKagCPpFS6CCcgW8-dItHbQPBtf6aMR9A",
  "authDomain": "portafolio-22b64.firebaseapp.com",
  "databaseURL": "https://portafolio-22b64-default-rtdb.firebaseio.com",
  "projectId": "portafolio-22b64",
  "storageBucket": "portafolio-22b64.appspot.com",
  "messagingSenderId": "203389337090",
  "appId": "1:203389337090:web:276614af6a2d1d342f711b",
  "measurementId": "G-WWW7HJBFRF"
}

# TODOS LOS COMANDOS SON DE LA LIBRERÍA PYREBASE4:
# https://github.com/nhorvath/Pyrebase4

firebase = pyrebase.initialize_app(config)

# ejemplo con auth
auth = firebase.auth()

try:
  usuario = auth.sign_in_with_email_and_password('jordan.terrazos@gmail.com','codigo2020')
  print(auth.get_account_info(usuario['idToken']))
  # Esto es para eliminar usuario
  # auth.delete_user_account(usuario['idToken'])
except:
  print("usuario o password inválidos")

# usuario2 = auth.sign_in_with_email_and_password('mr@gmail.com','monica')
# print(auth.send_email_verification(usuario2))

# print("enviando email de verificación")
# auth.send_email_verification(usuario['idToken'])

# Cambiando la contraseña del usuario
# auth.send_password_reset_email('jordan.terrazos@gmail.com')
# print("Se envió correo para resetear correo")

# creación de usuarios
# email = input("Ingrese Email: ")
# password = input("Ingrese Password: ")

# auth.create_user_with_email_and_password(email,password)
# print("Usuario creado con exito!")

from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

db = cliente['codigog11']
colAlumnos = db["alumnos"]
# alumnoId = colAlumnos.insert_one({"nombre":"Juan Menendez","email":"juan@gmail.com","nota":7})
# print("Nuevo Alumno: ",alumnoId)

# Consultar datos
for a in colAlumnos.find():
    print(a["nombre"] + " | " + a["email"])


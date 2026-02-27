from database import db

students = db["students"]

print("\n--- Limpiar colección ---")
students.delete_many({})  # elimina todo antes de empezar
print("Colección limpia")

# --------------------------
# INSERTAR UNO
# --------------------------
print("\n--- Insertar uno ---")

students.insert_one({
    "name": "hugofriasmtz",
    "country": "México",
    "city": "México City",
    "age": 23
})
print("Estudiante insertado:", students.find_one({"name": "hugofriasmtz"}))

# --------------------------
# INSERTAR VARIOS
# --------------------------
print("\n--- Insertar varios ---")

students.insert_many([
    {"name": "Karen", "country": "Brasil", "city": "São Paulo", "age": 22},
    {"name": "Erwin", "country": "Estados Unidos", "city": "New York", "age": 32},
    {"name": "Marcos", "country": "Francia", "city": "París", "age": 29},
    {"name": "Felipe", "country": "México", "city": "Monterrey", "age": 52}
])

# --------------------------
# MOSTRAR TODOS
# --------------------------
print("\n--- Mostrar todos ---")

for student in students.find():
    print(student)

# --------------------------
# FILTRO
# --------------------------
print("\n--- Solo BRASIL ---")

for student in students.find({"country": "Brasil"}):
    print(student)

# --------------------------
# OPERADOR
# --------------------------
print("\n--- Edad mayor a 30 ---")

for student in students.find({"age": {"$gt": 30}}):
    print(student)

# --------------------------
# ORDENAR
# --------------------------
print("\n--- Ordenado por edad ---")

for student in students.find().sort("age", 1):
    print(student)

# --------------------------
# ACTUALIZAR
# --------------------------
print("\n--- Actualizar edad 22 a 23 ---")

students.update_one(
    {"age": 22},
    {"$set": {"age": 23}}
)

for student in students.find():
    print(student)

# --------------------------
# ELIMINAR
# --------------------------
print("\n--- Eliminar Felipe ---")

students.delete_one({"name": "Felipe"})

for student in students.find():
    print(student)

from pymongo import MongoClient
from datetime import datetime
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["eduadaptiva"]

chats_collection = db["chats"]
emociones_collection = db["emociones"]
quiz_collection = db["quiz_resultados"]

def guardar_chat(nombre, mensaje, respuesta, materia):
    chats_collection.insert_one({
        "nombre": nombre,
        "mensaje": mensaje,
        "respuesta": respuesta,
        "materia": materia,
        "fecha": datetime.now()
    })

def guardar_emocion(nombre, emocion):
    emociones_collection.insert_one({
        "nombre": nombre,
        "emocion": emocion,
        "fecha": datetime.now()
    })

def guardar_quiz_mongo(nombre, materia, aciertos, total, nivel, fallas):
    quiz_collection.insert_one({
        "nombre": nombre,
        "materia": materia,
        "aciertos": aciertos,
        "total": total,
        "nivel": nivel,
        "fallas": fallas,
        "fecha": datetime.now()
    }) 
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import sqlite3
import requests

try:
    from google import genai
    client_ia = genai.Client(api_key="AQUI_PEGAS_TU_LLAVE_DE_GEMINI")
    TIENE_GEMINI = True
except:
    TIENE_GEMINI = False
    client_ia = None

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["eduadaptiva"]


def init_sqlite():
    conn = sqlite3.connect("edu.db")
    conn.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, materia TEXT)")
    conn.commit()
    conn.close()
init_sqlite()

def respuesta_chatbot(pregunta, materia="general"):
    if TIENE_GEMINI:
        try:
            prompt = f"Eres un maestro amigable para estudiantes de secundaria. Explica de forma sencilla, corta, con un ejemplo de la vida diaria. Materia: {materia}. Pregunta: {pregunta}"
            respuesta = client_ia.models.generate_content(model="gemini-2.0-flash", contents=prompt)
            return respuesta.text
        except:
            pass

    try:
        tema = pregunta.replace("que es", "").replace("¿", "").replace("?", "").strip()
        url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{tema}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json().get("extract", "")
    except:
        pass

    return f"Claro, te explico de {materia}: {pregunta} es un tema importante para entender como funciona el mundo. Tiene que ver con como la materia y la energia se transforman. ¿Quieres que te lo explique con un ejemplo de tu vida diaria?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    pregunta = data.get("mensaje", "")
    materia = data.get("materia", "general")
    nombre = data.get("nombre", "Vanessa")
    respuesta = respuesta_chatbot(pregunta, materia)
    db.chats.insert_one({"nombre": nombre, "mensaje": pregunta, "respuesta": respuesta, "materia": materia, "fecha": datetime.now()})
    return jsonify({"respuesta": respuesta})

@app.route("/emocion", methods=["POST"])
def emocion():
    data = request.get_json()
    db.emociones.insert_one({"nombre": data.get("nombre", "Vanessa"), "emocion": data.get("emocion", "bien"), "fecha": datetime.now()})
    return jsonify({"ok": True})

@app.route("/quiz", methods=["POST"])
def quiz():
    data = request.get_json()
    db.quiz_resultados.insert_one({"nombre": data.get("nombre", "Vanessa"), "materia": data.get("materia", "general"), "aciertos": data.get("aciertos", 0), "total": data.get("total", 3), "nivel": data.get("nivel", "Basico"), "fallas": data.get("fallas", []), "fecha": datetime.now()})
    return jsonify({"ok": True})

if __name__ == "__main__":
    print("✅ Abre tu página en: http://127.0.0.1:5000")
    app.run(debug=False, use_reloader=False) 
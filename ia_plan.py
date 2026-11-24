
PLANES = {
    "quimica": ["Día 1: Tabla periódica - ¿Qué es la N?", "Día 2: Qué es el Mol - La docena gigante", "Día 3: Masa Molar - Cómo sacarla", "Día 4: Conversiones Mol a Gramos", "Día 5: Conversiones a Litros y Partículas", "Día 6: Repaso de tus fallas", "Día 7: Examen simulado"],
    "mate": ["Día 1: Funciones", "Día 2: Límites", "Día 3: Derivada como pendiente", "Día 4: Reglas de derivación", "Día 5: Ejercicios tipo examen", "Día 6: Repaso", "Día 7: Examen"],
    "ingles": ["Día 1: Verbo To Be", "Día 2: Presente Simple", "Día 3: Preposiciones", "Día 4: Vocabulario", "Día 5: Habla con el bot", "Día 6: Repaso", "Día 7: Examen"],
    "fisica": ["Día 1: Movimiento", "Día 2: Velocidad", "Día 3: Fuerza F=mxa", "Día 4: Gravedad", "Día 5: Ejercicios", "Día 6: Repaso", "Día 7: Examen"],
    "biologia": ["Día 1: Célula", "Día 2: ADN", "Día 3: Fotosíntesis", "Día 4: Sistemas", "Día 5: Ecosistema", "Día 6: Repaso", "Día 7: Examen"],
    "historia": ["Día 1: Independencia 1810", "Día 2: Reforma", "Día 3: Porfiriato", "Día 4: Revolución 1910", "Día 5: Línea del tiempo", "Día 6: Repaso", "Día 7: Examen"],
    "espanol": ["Día 1: Sustantivos y verbos", "Día 2: Adjetivos", "Día 3: Idea principal", "Día 4: Sinónimos", "Día 5: Redacción", "Día 6: Repaso", "Día 7: Examen"],
    "computacion": ["Día 1: Algoritmos", "Día 2: Variables", "Día 3: If", "Día 4: Bucles", "Día 5: Python", "Día 6: Repaso", "Día 7: Proyecto"]
}

def generar_plan(materia, aciertos, total, animo, estilo, fallas):
    if total == 0:
        total = 1
    if aciertos <= 1:
        nivel = "Desde Cero"
    elif aciertos <= 2:
        nivel = "Básico"
    elif aciertos < total:
        nivel = "Intermedio"
    else:
        nivel = "Avanzado"

    consejo = ""
    if animo == "perdido":
        consejo = "Nos regresamos desde cero, paso a paso, sin prisa. "
    elif animo == "estresado":
        consejo = "Sesiones cortas de 15 min para no saturarte. "
    elif animo == "cansado":
        consejo = "Empezamos fácil para agarrar confianza. "
    else:
        consejo = "Vamos con buena actitud, tú puedes. "

    if estilo == "escuchando":
        consejo += "Te explico hablando, como plática."
    elif estilo == "viendo":
        consejo += "Te explico con dibujos y ejemplos visuales."
    elif estilo == "leyendo":
        consejo += "Te explico con textos cortos y claros."
    elif estilo == "practicando":
        consejo += "Tu plan es 80% práctica, aprendes haciendo."
    else:
        consejo += "Te explico con ejemplos de la vida real."

    pasos = PLANES.get(materia, PLANES["quimica"])
    return {"nivel": nivel, "aciertos": aciertos, "total": total, "fallas": fallas, "consejo": consejo, "pasos": pasos}
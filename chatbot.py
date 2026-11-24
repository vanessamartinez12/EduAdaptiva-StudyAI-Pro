import unicodedata
import random

ultimo_tema = {"tema": ""}

def limpiar(t):
    t = str(t).lower().strip()
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
    return t

def get_respuesta(pregunta, materia="quimica"):
    global ultimo_tema
    texto = limpiar(pregunta)
    materia = limpiar(materia or "quimica")
    if texto == "":
        return "Escríbeme tu duda, por ejemplo: ¿Qué es la masa molar?"

    if any(p in texto for p in ["no entiendo", "en todo", "nada", "perdido", "ayuda"]):
        return "Tranquila, vamos desde cero con un ejemplo fácil. ¿Empezamos con qué es una reacción o con qué es la masa molar? Dime cuál y te lo explico como si fuera la primera vez."

    if "gracias" in texto:
        return "De nada, ya le estás agarrando la onda, sigue así."

    if "formula" in texto and "masa" in texto:
        ultimo_tema["tema"] = "masa_molar"
        return "La fórmula de la masa es: gramos = moles x masa molar. Ejemplo real: Tienes 2 moles de NaCl, su masa molar es 58.5, entonces 2 x 58.5 = 117g. Esa es la que vas a usar. ¿Quieres que lo hagamos con tu número?"
    if "formula" in texto:
        if ultimo_tema["tema"] == "masa_molar":
            return "La fórmula que estábamos viendo es: gramos = moles x masa molar. Ejemplo: 2 x 58.5 = 117g."
        return "¿La fórmula de qué? Dime: 'fórmula de la masa' o 'fórmula de velocidad' y te la doy con ejemplo."

    if "y despues" in texto or texto == "y luego" or texto == "y":
        if ultimo_tema["tema"] == "masa_molar":
            return "Después de la masa molar sigue sacar los gramos: gramos = moles x masa molar. Ya tienes la fórmula, ahora solo multiplicas."
        return "¿Después de qué? Dime el tema y te digo qué sigue."

  
    if materia == "quimica":
        if "reaccion" in texto:
            ultimo_tema["tema"] = "reaccion"
            return "Una reacción es cuando los REACTIVOS se transforman en PRODUCTOS. Ejemplo: Papel + oxígeno -> ceniza + humo. Ya no es papel, es otra cosa."
        if "masa molar" in texto or texto == "en la masa" or "masa" in texto:
            ultimo_tema["tema"] = "masa_molar"
            return "La masa molar es lo que pesa 1 mol en gramos. Ejemplo: NaCl pesa 58.5 g/mol, o sea 1 mol = 58.5g y 2 moles = 117g. ¿Quieres que te dé su fórmula?"
        if "mol" in texto:
            return "1 mol = 6.022 x 10^23 partículas. Es como una docena gigante para átomos."
        if "atomo" in texto:
            return "Un átomo es la parte más pequeña de la materia. Tiene protones, neutrones y electrones."

    if materia == "mate":
        if "derivada" in texto:
            return "La derivada es qué tan rápido cambia algo. Ejemplo: Si tienes x^2, su derivada es 2x."
        if "limite" in texto:
            return "El límite es a lo que se acerca una función. Ejemplo: Si x se acerca a 2, x+1 se acerca a 3."

    if materia == "fisica" and "velocidad" in texto:
        return "Velocidad = distancia / tiempo. Ejemplo: 100m en 10s = 10 m/s."

    if materia == "ingles" and "to be" in texto:
        return "Fácil: I am, You are, He is, She is, We are, They are. Ejemplo: I am happy."

    
    opciones = [
        "Buena pregunta, dame un ejemplo de tu libro y te lo explico con ese número.",
        "A ver, dime con tus palabras qué parte no entiendes y te pongo otro ejemplo más fácil.",
        "¿Me pasas tu ejemplo de la tarea? Así te lo explico con tu mismo número, paso a paso."
    ]
    return random.choice(opciones)

def responder(pregunta, materia="quimica"):
    return get_respuesta(pregunta, materia)
def chat(mensaje, materia="quimica"):
    return get_respuesta(mensaje, materia) 
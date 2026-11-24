
import sqlite3

DB = "edu.db"

def crear_tablas():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        grupo TEXT,
        materia TEXT,
        animo TEXT,
        estilo TEXT,
        aciertos INTEGER,
        total INTEGER,
        fallas TEXT,
        nivel TEXT
    )
    """)
    con.commit()
    con.close()

def guardar_alumno(d):
    crear_tablas()
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT id FROM alumnos WHERE nombre=? AND materia=?", (d["nombre"], d["materia"]))
    existe = cur.fetchone()
    if existe:
        cur.execute("UPDATE alumnos SET grupo=?, animo=?, estilo=?, aciertos=?, total=?, fallas=?, nivel=? WHERE id=?",
                    (d["grupo"], d["animo"], d["estilo"], d["aciertos"], d["total"], d["fallas"], d["nivel"], existe[0]))
    else:
        cur.execute("INSERT INTO alumnos (nombre,grupo,materia,animo,estilo,aciertos,total,fallas,nivel) VALUES (?,?,?,?,?,?,?,?,?)",
                    (d["nombre"], d["grupo"], d["materia"], d["animo"], d["estilo"], d["aciertos"], d["total"], d["fallas"], d["nivel"]))
    con.commit()
    con.close()

def obtener_alumnos():
    crear_tablas()
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM alumnos ORDER BY id DESC")
    rows = cur.fetchall()
    con.close()
    return [dict(r) for r in rows]
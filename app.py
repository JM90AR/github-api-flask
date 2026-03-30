from flask import Flask
import requests
import psycopg2
from datetime import datetime

app = Flask(__name__)

BASE_URL = "https://api.github.com/users"

def get_db():
    return psycopg2.connect(
        host="db",
        database="midb",
        user="miguel",
        password="1234"
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id SERIAL PRIMARY KEY,
            usuario VARCHAR(100),
            fecha TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def registrar_consulta(usuario):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO consultas (usuario, fecha) VALUES (%s, %s)", 
                (usuario, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

@app.route("/perfil/<usuario>")
def perfil(usuario):
    registrar_consulta(usuario)
    data = requests.get(f"{BASE_URL}/{usuario}").json()
    return {
        "nombre": data["name"],
        "bio": data["bio"],
        "repos": data["public_repos"],
        "seguidores": data["followers"],
        "siguiendo": data["following"],
        "creado": data["created_at"]
    }

@app.route("/repos/<usuario>")
def repos(usuario):
    registrar_consulta(usuario)
    data = requests.get(f"{BASE_URL}/{usuario}/repos").json()
    return [
        {
            "nombre": r["name"],
            "descripcion": r["description"],
            "lenguaje": r["language"],
            "estrellas": r["stargazers_count"]
        }
        for r in data
    ]

@app.route("/resumen/<usuario>")
def resumen(usuario):
    registrar_consulta(usuario)
    perfil = requests.get(f"{BASE_URL}/{usuario}").json()
    repos = requests.get(f"{BASE_URL}/{usuario}/repos").json()
    return {
        "nombre": perfil["name"],
        "repos_count": perfil["public_repos"],
        "seguidores": perfil["followers"],
        "lenguajes": list(set(r["language"] for r in repos if r["language"]))
    }

@app.route("/historial")
def historial():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT usuario, fecha FROM consultas ORDER BY fecha DESC LIMIT 10")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"usuario": r[0], "fecha": str(r[1])} for r in rows]

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
from flask import Flask
import requests

app = Flask(__name__)

BASE_URL = "https://api.github.com/users"

@app.route("/perfil/<usuario>")
def perfil(usuario):
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
    perfil = requests.get(f"{BASE_URL}/{usuario}").json()
    repos = requests.get(f"{BASE_URL}/{usuario}/repos").json()
    return {
        "nombre": perfil["name"],
        "repos_count": perfil["public_repos"],
        "seguidores": perfil["followers"],
        "lenguajes": list(set(r["language"] for r in repos if r["language"]))
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
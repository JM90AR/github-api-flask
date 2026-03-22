# GitHub API Flask 🐙

A REST API built with **Python**, **Flask**, and **Docker** that queries real-time data from the GitHub API.

## 🔧 Technologies Used

- Python 3
- Flask (Web framework)
- Docker (Containerization)
- GitHub REST API

## 📌 Endpoints

| Route | Description |
|-------|-------------|
| `/perfil/<usuario>` | Returns name, bio, repos, followers |
| `/repos/<usuario>` | Lists all public repositories |
| `/resumen/<usuario>` | Summary with programming languages used |

## 🧠 How It Works

- Flask handles incoming GET requests
- Each route calls the GitHub API in real time
- Returns structured JSON responses

## 🗂 Example Usage

**Request:**
```
GET /perfil/torvalds
```

**Response:**
```json
{
  "nombre": "Linus Torvalds",
  "bio": null,
  "repos": 11,
  "seguidores": 292100,
  "siguiendo": 0,
  "creado": "2011-09-03T15:26:22Z"
}
```

## ⚙️ Setup Instructions

### With Docker (recommended)

1. Clone this repository:
```bash
git clone https://github.com/JM90AR/github-api-flask.git
cd github-api-flask
```

2. Build the image:
```bash
docker build -t github-api-flask .
```

3. Run the container:
```bash
docker run -p 5000:5000 github-api-flask
```

4. Open in your browser:
```
http://localhost:5000/perfil/<any_github_username>
```

### Without Docker

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

## 📫 Contact

Created by Miguel Alba  
Feel free to connect or reach out!

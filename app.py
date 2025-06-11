from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    imagens = [
        "IMG-20250611-WA0018.jpg",
        "IMG-20250611-WA0019.jpg",
        "IMG-20250611-WA0020.jpg",
        "IMG-20250611-WA0021.jpg",
        "IMG-20250611-WA0022.jpg",
        "IMG-20250611-WA0023.jpg",
        "IMG-20250611-WA0024.jpg",
        "IMG-20250611-WA0025.jpg",
        "IMG-20250611-WA0026.jpg",
        "IMG-20250611-WA0027.jpg",
        "IMG-20250611-WA0028.jpg",
        "IMG-20250611-WA0029.jpg",
        "IMG-20250611-WA0030.jpg",
        "IMG-20250611-WA0031.jpg",
        "IMG-20250611-WA0032.jpg",
        "IMG-20250611-WA0033.jpg",
        "IMG-20250611-WA0034.jpg",
        "IMG-20250611-WA0035.jpg",
        "IMG-20250611-WA0036.jpg",
        "IMG-20250611-WA0037.jpg",
        "IMG-20250611-WA0038.jpg",
        "IMG-20250611-WA0039.jpg",
        "IMG-20250611-WA0040.jpg",
        "IMG-20250611-WA0041.jpg",
        "IMG-20250611-WA0042.jpg",
        "IMG-20250611-WA0043.jpg",
        "IMG-20250611-WA0044.jpg",
        "IMG-20250611-WA0045.jpg"
    ]
    data_alvo = "2023-01-15T00:15:00"  # Altere aqui a data desejada
    return render_template("index.html", imagens=imagens, data_alvo=data_alvo)

if __name__ == "__main__":
    app.run(debug=True)

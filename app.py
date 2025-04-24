from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Application sécurisée dans un conteneur Docker."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

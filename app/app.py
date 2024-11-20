from flask import Flask, jsonify
from flask_cors import CORS

from categorization.routes import categorization_bp

# cria uma instância do Flask
app = Flask(__name__)
CORS(app)

# registra o blueprint da rota de sugestão
app.register_blueprint(categorization_bp)

if __name__ == '__main__':
    app.run(debug=True)

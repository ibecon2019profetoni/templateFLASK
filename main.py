from flask import Flask
from flask import render_template
from flask import request

from paquete.conexion_mysql import *

app = Flask(__name__)

# rutas
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        libro = request.form['libro']

        for titulo, precio, autor in datos:
            if titulo.lower() == libro.lower():
                return render_template('index.html', titulo=titulo,precio=precio,autor=autor)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
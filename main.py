from flask import Flask
from flask import render_template
from flask import request

from paquete.conexion_mysql import *

app = Flask(__name__)

# rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        libro = request.form['libro']

        consulta = conexion_MYSQL(libro)

        return render_template('index.html', titulo=consulta[0][0], precio=consulta[0][1], autor=consulta[0][2])

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

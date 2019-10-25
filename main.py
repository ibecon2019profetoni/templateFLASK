from flask import Flask
from flask import render_template
from flask import request

from paquete.conexion import Bd

app = Flask(__name__)

# rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            libro = request.form['libro']

            busqueda_libros = Bd('localhost', 'root', 'root', 'libreriaToni')
            consulta = busqueda_libros.query(
                f'SELECT b.title, b.price, a.name FROM books AS b INNER JOIN authors AS a ON a.author_id = b.author_id WHERE b.title LIKE "%{libro}%" ORDER BY RAND() LIMIT 5')
         

            return render_template('index.html', consulta=consulta)

        except IndexError:
            return 'No existe, en la base de datos.'

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

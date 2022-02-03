from flask import Flask, render_template

app = Flask( __name__)

#1 http://127.0.0.1:5000/
@app.route( '/', methods=['GET'] )
def paginaInicial():
    return render_template( "index.html", fila=8, columna=8, color1= 'red', color2= 'black'  )


#2
@app.route( '/<int:i>', methods=['GET'] )
def segundo(i):
    return render_template( "index.html", fila=i, columna=8, color1= 'red', color2= 'black' )


#3 BONUS NINJA: Haz que otra ruta acepte 2 parámetro "//"
# renderiza un tablero de ajedrez con x filas e y columnas Las columnas, con colores alternos
@app.route( '/<int:i>/<int:j>', methods=['GET'] )
def tercero(i,j):
    return render_template( "index.html", fila=i, columna=j, color1= 'red', color2= 'black' )

#4
@app.route( '/<int:i>/<int:j>/<string:color1>', methods=['GET'] )
def cuarto(i,j,color1):
    return render_template( "index.html", fila=i, columna=j, color1= color1, color2= 'black' )


#5 BONUS SENSEI: Haz que otra ruta acepte 4 parámetro "////"
# renderiza un tablero de ajedrez con x filas e y columnas, con colores alternos, color1 y color2
@app.route( '/<int:i>/<int:j>/<string:color1>/<string:color2>', methods=['GET'] )
def quinto(i,j,color1,color2):
    return render_template( "index.html", fila=i, columna=j, color1= color1, color2= color2 )


if __name__ == "__main__":
    app.run( debug=True )



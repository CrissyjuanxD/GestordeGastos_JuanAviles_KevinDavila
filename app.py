from flask import Flask, render_template, request
from categorias import GestorGastos
app = Flask(__name__)
usuario = GestorGastos()

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/agregar_gastos', methods=['POST'])
def agregar_gastos():
    categoria = request.form['categoria']
    nombre = request.form['nombre']
    monto = request.form['monto']
    fecha = request.form['fecha']
    gastos_input = request.form['gastos']
    try:
        gastos = float(gastos_input)
        if gastos != round(gastos, 2):
            error = "El valor de gastos no es un número válido."
            return render_template('index.html', text=error, lista=usuario.gastos)
    except ValueError:
        # Manejo de error si no se pudo convertir a un entero
        error = "El valor de gastos no es un número válido."
        return render_template('index.html', text=error, lista=usuario.gastos)

    output = usuario.agregar_gastos(categoria, nombre, monto, fecha)
    return render_template('index.html', text=f'Gasto agregado con éxito', lista=output)

@app.route('/gastos_mensuales', methods=['POST'])
def gastos_mensuales():
    meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE',
             'NOVIEMBRE', 'DICIEMBRE']
    fecha = request.form['fecha']
    mes = fecha.split('-')
    mes = int(mes[1])
    mes = meses[mes - 1]
    resume = usuario.visualizar_resumen_mensual(fecha)
    if len(resume) > 0:
        categorias = list(resume.keys())
        monto = list(resume.values())
        total = sum(monto)
        return render_template('index.html', categorias=categorias, gastos=monto, total=total, mes=mes)

if __name__ == '__main__':
    app.run()

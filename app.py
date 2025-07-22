from flask import Flask, render_template, abort
from models import get_about, get_servicios, get_portafolio, get_proyecto_por_nombre, get_contacto, get_especialidades, get_lenguajes

app = Flask(__name__)

@app.route('/')
def home():
    about = get_about()
    espe = get_especialidades()
    leng = get_lenguajes()
    return render_template('index.html', about=about, espe=espe, leng=leng)

@app.route('/servicios') 
def servicios():
    svc = get_servicios()
    return render_template('servicio.html', svc=svc) 

@app.route('/trabajos')
def trabajos():
    portfolio = get_portafolio()
    return render_template('Trabajos.html', portfolio=portfolio)

@app.route('/trabajos/<nombre>')
def trabajo_detalle(nombre):
    trabajo = get_proyecto_por_nombre(nombre)
    if not trabajo:
        abort(404)
    return render_template('Trabajosdetalle.html', portfolio=trabajo)

@app.route('/contacto')
def contacto():
    about = get_about()
    contacto = get_contacto()
    return render_template('Contacto.html', about=about, contacto=contacto)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)

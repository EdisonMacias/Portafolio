import json

def load_json(file):
    with open(f'data/{file}', encoding='utf-8') as f:
        return json.load(f)

# Obtener About
def get_about():
    return load_json('about.json')

# Especialidades por About
def get_especialidades():
    return load_json('especialidades.json')

# Lenguajes por About
def get_lenguajes():
    return load_json('lenguajes.json')

# Servicios por About
def get_servicios():
    return load_json('servicios.json')

# Contacto por About
def get_contacto():
    return load_json('contacto.json')

# Portafolio
def get_portafolio():
    return load_json('portafolio.json')

def get_proyecto_por_nombre(nombre):
    proyectos = get_portafolio()
    return next((p for p in proyectos if p["nom"] == nombre), None)

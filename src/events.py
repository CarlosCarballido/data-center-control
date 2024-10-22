import clips

def agregar_zona(env, nombre, temperatura, humedad, estado_ac, acceso):
    env.assert_string(f'(zona (nombre "{nombre}") (temperatura {temperatura}) (humedad {humedad}) (estado_ac {estado_ac}) (acceso {acceso}))')

def modificar_zona(env, nombre, temperatura=None, humedad=None, estado_ac=None, acceso=None):
    for fact in env.facts():
        if "zona" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(zona (nombre "{nombre}")'
                new_fact += f' (temperatura {temperatura if temperatura else fact["temperatura"]})'
                new_fact += f' (humedad {humedad if humedad else fact["humedad"]})'
                new_fact += f' (estado_ac {estado_ac if estado_ac else fact["estado_ac"]})'
                new_fact += f' (acceso {acceso if acceso else fact["acceso"]}))'
                env.assert_string(new_fact)
           
def agregar_rack(env, nombre, zona, tipo, estado):
    env.assert_string(f'(rack (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')
    
def modificar_rack(env, nombre, zona=None, tipo=None, estado=None):
    for fact in env.facts():
        if "rack" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(rack (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado else fact["estado"]}))'
                env.assert_string(new_fact)
                
def agregar_accion(env, nombre, zona, tipo, estado):
    env.assert_string(f'(accion (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')
    
def modificar_accion(env, nombre, zona=None, tipo=None, estado=None):
    for fact in env.facts():
        if "accion" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(accion (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado else fact["estado"]}))'
                env.assert_string(new_fact)
                
def agregar_desastre(env, nombre, zona, tipo, estado):
    env.assert_string(f'(desastre (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')
    
def moficar_desastre(env, nombre, zona=None, tipo=None, estado=None):
    for fact in env.facts():
        if "desastre" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(desastre (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado else fact["estado"]}))'
                env.assert_string(new_fact)
                
def agregar_sensor(env, nombre, zona, tipo, valor):
    env.assert_string(f'(sensor (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (valor {valor}))')
    
def modificar_sensor(env, nombre, zona=None, tipo=None, valor=None):
    for fact in env.facts():
        if "sensor" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(sensor (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (valor {valor if valor else fact["valor"]}))'
                env.assert_string(new_fact)
     
def agregar_actuador(env, nombre, zona, tipo, estado):
    env.assert_string(f'(actuador (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')
    
def modificar_actuador(env, nombre, zona=None, tipo=None, estado=None):
    for fact in env.facts():
        if "actuador" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(actuador (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado else fact["estado"]}))'
                env.assert_string(new_fact)
                
import clips

def agregar_zona(env, nombre, temperatura, humedad, estado_ac, acceso):
    env.assert_string(f'(zona (nombre "{nombre}") (temperatura {temperatura}) (humedad {humedad}) (estado_ac {estado_ac}) (acceso {acceso}))')

def modificar_zona(env, nombre, temperatura=None, humedad=None, estado_ac=None, acceso=None):
    for fact in env.facts():
        if fact.template.name == "zona" and fact["nombre"] == nombre:
            env.retract(fact)
            new_fact = f'(zona (nombre "{nombre}")'
            new_fact += f' (temperatura {temperatura if temperatura is not None else fact["temperatura"]})'
            new_fact += f' (humedad {humedad if humedad is not None else fact["humedad"]})'
            new_fact += f' (estado_ac {estado_ac if estado_ac is not None else fact["estado_ac"]})'
            new_fact += f' (acceso {acceso if acceso is not None else fact["acceso"]}))'
            env.assert_string(new_fact)

def agregar_rack(env, id, voltaje):
    env.assert_string(f'(rack (id "{id}") (voltaje {voltaje}))')

def modificar_rack(env, id, voltaje=None):
    for fact in env.facts():
        if fact.template.name == "rack" and fact["id"] == id:
            env.retract(fact)
            new_fact = f'(rack (id "{id}") (voltaje {voltaje if voltaje is not None else fact["voltaje"]}))'
            env.assert_string(new_fact)

def agregar_accion(env, tipo, comando, nombre):
    env.assert_string(f'(accion (tipo "{tipo}") (comando "{comando}") (nombre "{nombre}"))')

def modificar_accion(env, nombre, tipo=None, comando=None):
    for fact in env.facts():
        if fact.template.name == "accion" and fact["nombre"] == nombre:
            env.retract(fact)
            new_fact = f'(accion (nombre "{nombre}")'
            new_fact += f' (tipo "{tipo if tipo is not None else fact["tipo"]}")'
            new_fact += f' (comando "{comando if comando is not None else fact["comando"]}"))'
            env.assert_string(new_fact)

def agregar_desastre(env, tipo, zona):
    env.assert_string(f'(desastre (tipo "{tipo}") (zona "{zona}"))')

def modificar_desastre(env, zona, tipo=None):
    for fact in env.facts():
        if fact.template.name == "desastre" and fact["zona"] == zona:
            env.retract(fact)
            new_fact = f'(desastre (tipo "{tipo if tipo is not None else fact["tipo"]}") (zona "{zona}"))'
            env.assert_string(new_fact)

def agregar_sensor(env, tipo, value, zona):
    env.assert_string(f'(sensor (tipo "{tipo}") (value {value}) (zona "{zona}"))')

def modificar_sensor(env, tipo, zona, value=None):
    for fact in env.facts():
        if fact.template.name == "sensor" and fact["tipo"] == tipo and fact["zona"] == zona:
            env.retract(fact)
            new_fact = f'(sensor (tipo "{tipo}") (value {value if value is not None else fact["value"]}) (zona "{zona}"))'
            env.assert_string(new_fact)

def agregar_actuador(env, tipo, valor, zona):
    env.assert_string(f'(actuadores (tipo "{tipo}") (valor {valor}) (zona "{zona}"))')

def modificar_actuador(env, tipo, zona, valor=None):
    for fact in env.facts():
        if fact.template.name == "actuadores" and fact["tipo"] == tipo and fact["zona"] == zona:
            env.retract(fact)
            new_fact = f'(actuadores (tipo "{tipo}") (valor {valor if valor is not None else fact["valor"]}) (zona "{zona}"))'
            env.assert_string(new_fact)

       
def agregar_humo(env, nombre, zona, tipo, estado):
    env.assert_string(f'(humo (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')
    
def modificar_humo(env, nombre, zona=None, tipo=None, estado=None):
    for fact in env.facts():
        if "humo" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(humo (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado else fact["estado"]}))'
                env.assert_string(new_fact)       

def agregar_sensor_humo(env, zona):
    env.assert_string(f'(sensor (tipo "humo") (value "si") (zona "{zona}"))')
    
def modificar_sensor_humo(env, zona, value=None):
    for fact in env.facts():
        if fact.template.name == "sensor" and fact["tipo"] == "humo" and fact["zona"] == zona:
            env.retract(fact)
            new_fact = f'(sensor (tipo "humo") (value {"si" if value is None else value}) (zona "{zona}"))'
            env.assert_string(new_fact)
                
def agregar_agua(env, nombre, zona, tipo, estado):
    env.assert_string(f'(agua (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')
    
def modificar_agua(env, nombre, zona=None, tipo=None, estado=None):
    for fact in env.facts():
        if "agua" in str(fact):
            if fact["nombre"] == nombre:
                env.retract(fact)
                new_fact = f'(agua (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado else fact["estado"]}))'
                env.assert_string(new_fact)
                
def agregar_sensor_agua(env, zona):
    env.assert_string(f'(sensor (tipo "agua") (value "si") (zona "{zona}"))')
    
def modificar_sensor_agua(env, zona, value=None):
    for fact in env.facts():
        if fact.template.name == "sensor" and fact["tipo"] == "agua" and fact["zona"] == zona:
            env.retract(fact)
            new_fact = f'(sensor (tipo "agua") (value {"si" if value is None else value}) (zona "{zona}"))'
            env.assert_string(new_fact)
import clips

class EventsManager:
    def __init__(self):
        self.env = clips.Environment()
        
    def reset(self):
        self.env.reset()

    def agregar_zona(self, nombre, temperatura, humedad, estado_ac, acceso):
        self.env.assert_string(f'(zona (nombre "{nombre}") (temperatura {temperatura}) (humedad {humedad}) (estado_ac {estado_ac}) (acceso {acceso}))')

    def modificar_zona(self, nombre, temperatura=None, humedad=None, estado_ac=None, acceso=None):
        hecho_existente = None

        # Buscar el hecho correspondiente al nombre de la zona
        for fact in self.env.facts():
            if fact.template.name == "zona" and fact["nombre"] == nombre:
                hecho_existente = fact
                break

        # Si encontramos el hecho, añadimos un nuevo hecho con los valores modificados
        if hecho_existente:
            new_fact = f'(zona (nombre "{nombre}")'
            new_fact += f' (temperatura {temperatura if temperatura is not None else hecho_existente["temperatura"]})'
            new_fact += f' (humedad {humedad if humedad is not None else hecho_existente["humedad"]})'
            new_fact += f' (estado_ac {estado_ac if estado_ac is not None else hecho_existente["estado_ac"]})'

            # Solo agregar "acceso" si se proporciona un nuevo valor
            if acceso is not None:
                new_fact += f' (acceso {acceso})'
            else:
                new_fact += f' (acceso {hecho_existente["acceso"]})'

            new_fact += ')'

            # Insertar el nuevo hecho
            self.env.assert_string(new_fact)
            
            self.env.run()
            
        else:
            print(f"Zona {nombre} no encontrada.")


    def agregar_rack(self, id, voltaje):
        self.env.assert_string(f'(rack (id "{id}") (voltaje {voltaje}))')

    def modificar_rack(self, id, voltaje=None):
        for fact in self.env.facts():
            if fact.template.name == "rack" and fact["id"] == id:
                self.env.retract(fact)
                new_fact = f'(rack (id "{id}") (voltaje {voltaje if voltaje is not None else fact["voltaje"]}))'
                self.env.assert_string(new_fact)

    def agregar_accion(self, tipo, comando, nombre):
        self.env.assert_string(f'(accion (tipo "{tipo}") (comando "{comando}") (nombre "{nombre}"))')

    def modificar_accion(self, nombre, tipo=None, comando=None):
        for fact in self.env.facts():
            if fact.template.name == "accion" and fact["nombre"] == nombre:
                self.env.retract(fact)
                new_fact = f'(accion (nombre "{nombre}")'
                new_fact += f' (tipo "{tipo if tipo is not None else fact["tipo"]}")'
                new_fact += f' (comando "{comando if comando is not None else fact["comando"]}"))'
                self.env.assert_string(new_fact)

    def agregar_desastre(self, tipo, zona):
        self.env.assert_string(f'(desastre (tipo "{tipo}") (zona "{zona}"))')

    def modificar_desastre(self, zona, tipo=None):
        for fact in self.env.facts():
            if fact.template.name == "desastre" and fact["zona"] == zona:
                self.env.retract(fact)
                new_fact = f'(desastre (tipo "{tipo if tipo is not None else fact["tipo"]}") (zona "{zona}"))'
                self.env.assert_string(new_fact)

    def agregar_sensor(self, tipo, value, zona):
        self.env.assert_string(f'(sensor (tipo "{tipo}") (value {value}) (zona "{zona}"))')

    def modificar_sensor(self, tipo, zona, value=None):
        for fact in self.env.facts():
            if fact.template.name == "sensor" and fact["tipo"] == tipo and fact["zona"] == zona:
                self.env.retract(fact)
                new_fact = f'(sensor (tipo "{tipo}") (value {value if value is not None else fact["value"]}) (zona "{zona}"))'
                self.env.assert_string(new_fact)

    def agregar_actuador(self, tipo, valor, zona):
        self.env.assert_string(f'(actuadores (tipo "{tipo}") (valor {valor}) (zona "{zona}"))')

    def modificar_actuador(self, tipo, zona, valor=None):
        for fact in self.env.facts():
            if fact.template.name == "actuadores" and fact["tipo"] == tipo and fact["zona"] == zona:
                self.env.retract(fact)
                new_fact = f'(actuadores (tipo "{tipo}") (valor {valor if valor is not None else fact["valor"]}) (zona "{zona}"))'
                self.env.assert_string(new_fact)

    def agregar_humo(self, nombre, zona, tipo, estado):
        self.env.assert_string(f'(humo (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')

    def modificar_humo(self, nombre, zona=None, tipo=None, estado=None):
        for fact in self.env.facts():
            if fact.template.name == "humo" and fact["nombre"] == nombre:
                self.env.retract(fact)
                new_fact = f'(humo (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona is not None else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo is not None else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado is not None else fact["estado"]}))'
                self.env.assert_string(new_fact)

    def agregar_sensor_humo(self, zona):
        self.env.assert_string(f'(sensor (tipo "humo") (value "si") (zona "{zona}"))')

    def modificar_sensor_humo(self, zona, value=None):
        for fact in self.env.facts():
            if fact.template.name == "sensor" and fact["tipo"] == "humo" and fact["zona"] == zona:
                self.env.retract(fact)
                new_fact = f'(sensor (tipo "humo") (value {"si" if value is None else value}) (zona "{zona}"))'
                self.env.assert_string(new_fact)

    def agregar_agua(self, nombre, zona, tipo, estado):
        self.env.assert_string(f'(agua (nombre "{nombre}") (zona "{zona}") (tipo "{tipo}") (estado {estado}))')

    def modificar_agua(self, nombre, zona=None, tipo=None, estado=None):
        for fact in self.env.facts():
            if fact.template.name == "agua" and fact["nombre"] == nombre:
                self.env.retract(fact)
                new_fact = f'(agua (nombre "{nombre}")'
                new_fact += f' (zona "{zona if zona is not None else fact["zona"]}")'
                new_fact += f' (tipo "{tipo if tipo is not None else fact["tipo"]}")'
                new_fact += f' (estado {estado if estado is not None else fact["estado"]}))'
                self.env.assert_string(new_fact)

    def agregar_sensor_agua(self, zona):
        self.env.assert_string(f'(sensor (tipo "agua") (value "si") (zona "{zona}"))')

    def modificar_sensor_agua(self, zona, value=None):
        for fact in self.env.facts():
            if fact.template.name == "sensor" and fact["tipo"] == "agua" and fact["zona"] == zona:
                self.env.retract(fact)
                new_fact = f'(sensor (tipo "agua") (value {"si" if value is None else value}) (zona "{zona}"))'
                self.env.assert_string(new_fact)

    def run(self):
        self.env.run()
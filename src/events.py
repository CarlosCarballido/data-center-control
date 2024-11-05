import clips

class EventsManager:
    def __init__(self, env):
        self.env = env
        
    def reset(self):
        self.env.reset()

    def agregar_zona(self, nombre, temperatura, humedad, estado_ac, nivel_acceso):
        if nivel_acceso is None:
            nivel_acceso = 1
        self.env.assert_string(f'(zona (nombre "{nombre}") (temperatura {temperatura}) (humedad {humedad}) (estado_ac "{estado_ac}") (acceso "{nivel_acceso}"))')

    def modificar_zona(self, nombre, temperatura=None, humedad=None, estado_ac=None, acceso=None, nivel_acceso=None):
        # Buscar el hecho correspondiente y eliminarlo, luego agregar uno nuevo con los valores actualizados
        fact_to_modify = None
        for fact in self.env.facts():
            if fact.template.name == "zona" and fact["nombre"] == nombre:
                fact_to_modify = fact
                break

        if fact_to_modify:
            # Extraer los valores actuales del hecho
            current_temperatura = fact_to_modify["temperatura"]
            current_humedad = fact_to_modify["humedad"]
            current_estado_ac = fact_to_modify["estado_ac"]
            current_acceso = fact_to_modify["acceso"] if "acceso" in fact_to_modify else 1  # Valor por defecto 1
            current_nivel_acceso = fact_to_modify["nivel_acceso"] if fact_to_modify["nivel_acceso"] is not None else 1  # Valor por defecto 1

            # Utilizar los valores actuales si no se proporcionan nuevos valores
            new_temperatura = temperatura if temperatura is not None else current_temperatura
            new_humedad = humedad if humedad is not None else current_humedad
            new_estado_ac = estado_ac if estado_ac is not None else current_estado_ac
            new_acceso = acceso if acceso is not None else current_acceso
            new_nivel_acceso = nivel_acceso if nivel_acceso is not None else current_nivel_acceso

            # Eliminar el hecho actual
            self.env.assert_string(f"(retract {fact_to_modify.index})")

            # Agregar el hecho modificado con valores actualizados
            self.env.assert_string(f"(zona (nombre \"{nombre}\") (temperatura {new_temperatura}) (humedad {new_humedad}) (estado_ac \"{new_estado_ac}\") (nivel_acceso {new_nivel_acceso}))")
            
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
        self.env.assert_string(f'(sensor (tipo "{tipo}") (value "{value}") (zona "{zona}"))')

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

    def agregar_sensor_humo(self, zona):
        self.env.assert_string(f'(sensor (tipo "humo") (value "si") (zona "{zona}"))')

    def modificar_sensor_humo(self, zona, value=None):
        for fact in self.env.facts():
            if fact.template.name == "sensor" and fact["tipo"] == "humo" and fact["zona"] == zona:
                self.env.retract(fact)
                new_fact = f'(sensor (tipo "humo") (value {"si" if value is None else value}) (zona "{zona}"))'
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

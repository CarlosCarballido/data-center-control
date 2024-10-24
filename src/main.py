import clips
from events import EventsManager
import threading
import random
import time
import os

def cargar_reglas():
    env = clips.Environment()
    
    try:
        base_path = os.path.dirname(__file__)
        env.load(os.path.join(base_path, '../clips/control_reglas.clp'))
        print("Reglas cargadas correctamente.")
    except Exception as e:
        print(f"Error cargando control_reglas.clp: {e}")
    
    try:
        env.load(os.path.join(base_path, '../clips/hechos_iniciales.clp'))
        print("Hechos iniciales cargados correctamente.")
    except Exception as e:
        print(f"Error cargando hechos_iniciales.clp: {e}")
        
    env.reset()
    return env

def ejecutar_reglas(env):
    env.run()
    manejar_alertas(env)  # Revisar hechos después de ejecutar reglas

def generar_eventos_aleatorios(manager):
    zonas = ["Cafeteria", "zona2", "zona3"]
    while True:
        # Seleccionar aleatoriamente una zona y un tipo de evento
        zona = random.choice(zonas)
        temperatura = random.randint(15, 35)  # Temperatura aleatoria entre 15 y 35
        humedad = random.choices([random.randint(30, 60), random.randint(70, 80)], weights=[80, 20])[0]
        estado_ac = random.choice(["encendido", "apagado"])
        acceso = random.choice(["abierto", "cerrado"])

        # Verificar si la zona existe, si no, agregarla
        existe = any(fact.template.name == "zona" and fact["nombre"] == zona for fact in manager.env.facts())
        if not existe:
            manager.agregar_zona(zona, temperatura, humedad, estado_ac, acceso)
        else:
            # Modificar la zona seleccionada con valores aleatorios
            manager.modificar_zona(zona, temperatura=temperatura, humedad=humedad, estado_ac=estado_ac, acceso=acceso)
        
        # Generar eventos adicionales aleatorios
        tipo_sensor = random.choice(["humo", "agua"])
        if random.choice([True, False]):
            manager.agregar_sensor(tipo_sensor, "si", zona)
        
        ejecutar_reglas(manager.env)
        time.sleep(3)

def manejar_alertas(env):
    hechos_para_modificar = []

    for fact in list(env.facts()):
        if fact.template.name == "accion" and fact["tipo"] == "alerta":
            # Verificar si la alerta ya ha sido resuelta
            try:
                resuelta = fact["resuelta"]
            except KeyError:
                resuelta = False

            if not resuelta:
                alerta_msg = f"Alerta: {fact['comando'].replace('_', ' ')} en la {fact['nombre']}"
                print(alerta_msg)

                # Simular la reparación de la alerta
                if fact['comando'] not in ["acceso_abierto", "acceso_cerrado"]:
                    time.sleep(2)
                    print(f"Reparación completada para: {alerta_msg}")
                    hechos_para_modificar.append(fact)

    # Modificar los hechos que causaron la alerta
    for fact in hechos_para_modificar:
        # Actualizar el valor del sensor correspondiente a un valor aceptable (por ejemplo, 50)
        for sensor_fact in env.facts():
            if sensor_fact.template.name == "sensor" and sensor_fact["zona"] == fact["nombre"] and sensor_fact["tipo"] == "humedad":
                # Modificar el valor del sensor directamente
                sensor_fact.modify_slots(value=50)
                break

        # Añadir o modificar el slot `resuelta` en el hecho de alerta para indicar que ha sido gestionado
        fact.modify_slots(resuelta=True)


if __name__ == "__main__":
    env = cargar_reglas()
    manager = EventsManager()
    manager.env = env
    
    ejecutar_reglas(env)

    # Hilo para generar eventos aleatorios continuamente
    evento_hilo = threading.Thread(target=generar_eventos_aleatorios, args=(manager,))
    evento_hilo.daemon = True
    evento_hilo.start()

    while True:
        time.sleep(3)

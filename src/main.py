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

def generar_eventos_aleatorios(manager):
    zonas = ["Cafeteria", "Pasillo", "Oficina", "Sala de Pruebas", "Sala de Servidores", "Sala de Control"]
    while True:
        zona = random.choice(zonas)
        temperatura = random.randint(15, 35)
        humedad = random.choices([random.randint(30, 60), random.randint(70, 80)], weights=[80, 20])[0]
        estado_ac = random.choice(["encendido", "apagado"])
        nivel_acceso = random.randint(1, 3)

        existe = any(fact.template.name == "zona" and fact["nombre"] == zona for fact in manager.env.facts())
        if not existe:
            manager.agregar_zona(zona, temperatura, humedad, estado_ac, nivel_acceso)
        else:
            manager.modificar_zona(zona, temperatura=temperatura, humedad=humedad, estado_ac=estado_ac, nivel_acceso=nivel_acceso)

        tipo_sensor = random.choice(["humo", "agua"])
        if random.choice([True, False]):
            manager.agregar_sensor(tipo_sensor, "si", zona)

        ejecutar_reglas(manager.env)
        time.sleep(3)



if __name__ == "__main__":
    env = cargar_reglas()
    manager = EventsManager(env)

    ejecutar_reglas(env)

    generar_eventos = input("¿Quieres que se generen eventos aleatorios? (s/n): ").strip().lower()
    
    if generar_eventos == 's':
        evento_hilo = threading.Thread(target=generar_eventos_aleatorios, args=(manager,))
        evento_hilo.daemon = True
        evento_hilo.start()

        while True:
            time.sleep(3)

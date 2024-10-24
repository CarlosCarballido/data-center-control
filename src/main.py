import clips
from events import EventsManager
import threading
import random
import time

def cargar_reglas():
    env = clips.Environment()
    
    try:
        env.load('clips/control_reglas.clp')
        print("Reglas cargadas correctamente.")
    except Exception as e:
        print(f"Error cargando control_reglas.clp: {e}")
    
    try:
        env.load('clips/hechos_iniciales.clp')
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
        humedad = random.randint(30, 80)      # Humedad aleatoria entre 30 y 80
        estado_ac = random.choice(["encendido", "apagado"])
        acceso = random.choice(["abierto", "cerrado"])

        # Verificar si la zona existe, si no, agregarla
        existe = any(fact.template.name == "zona" and fact["nombre"] == zona for fact in manager.env.facts())
        if not existe:
            manager.agregar_zona(zona, temperatura, humedad, estado_ac, acceso)
        else:
            # Modificar la zona seleccionada con valores aleatorios
            manager.modificar_zona(zona, temperatura=temperatura, humedad=humedad, estado_ac=estado_ac, acceso=acceso)
        
        ejecutar_reglas(manager.env)

        time.sleep(3)
        
        import os
        os.system('clear')

def manejar_alertas(env):
    hechos_para_modificar = []
    for fact in list(env.facts()):
        if fact.template.name == "accion" and fact["tipo"] == "alerta":
            alerta_msg = f"Alerta: {fact['comando'].replace('_', ' ')} en la {fact['nombre']}"
            print(alerta_msg)
            if fact['comando'] != "acceso_abierto" and fact['comando'] != "acceso_cerrado":
                time.sleep(2)
                print(f"Reparación completada para: {alerta_msg}")
                hechos_para_modificar.append(fact)
    
    for fact in hechos_para_modificar:
        env.assert_string(f"(accion (tipo reparada) (comando {fact['comando']}) (nombre {fact['nombre']}))")

if __name__ == "__main__":
    env = cargar_reglas()
    manager = EventsManager()
    manager.env = env
    
    ejecutar_reglas(env)

    evento_hilo = threading.Thread(target=generar_eventos_aleatorios, args=(manager,))
    evento_hilo.daemon = True
    evento_hilo.start()

    while True:
        time.sleep(3)

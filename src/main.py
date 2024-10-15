import clips

def cargar_reglas():
    # Crear el entorno de CLIPS
    env = clips.Environment()
    
    # Cargar los archivos CLP
    env.load('clips/control_reglas.clp')
    env.load('clips/hechos_iniciales.clp')
    
    # Retornar el entorno cargado
    return env

def ejecutar_reglas(env):
    # Ejecutar el motor de reglas
    env.run()
    
    # Imprimir los hechos generados
    for fact in env.facts():
        print(fact)

if __name__ == "__main__":
    # Cargar reglas y hechos
    env = cargar_reglas()
    
    # Ejecutar las reglas
    ejecutar_reglas(env)

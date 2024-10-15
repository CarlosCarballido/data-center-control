import clips

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
    
    # Mostrar los hechos antes de ejecutar
    print("Hechos iniciales:")
    for fact in env.facts():
        print(fact)
    
    return env

def ejecutar_reglas(env):
    print("Ejecutando reglas...")
    env.run()

    print("Hechos generados:")
    for fact in env.facts():
        print(fact)


if __name__ == "__main__":
    env = cargar_reglas()
    
    ejecutar_reglas(env)

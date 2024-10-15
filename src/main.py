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
        
    env.reset()
    
    print("\nHechos iniciales:")
    for fact in env.facts():
        print(fact)
    
    return env

def ejecutar_reglas(env):
    print("\nEjecutando reglas...")
    env.run()

    print("\nHechos generados:")
    for fact in env.facts():
        print(fact)

if __name__ == "__main__":
    env = cargar_reglas()
    
    ejecutar_reglas(env)

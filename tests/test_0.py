import clips
import pytest

def test_ejecucion_reglas():
    env = clips.Environment()
    
    # Cargar las reglas y hechos de prueba
    env.load('clips/control_reglas.clp')
    env.load('clips/hechos_iniciales.clp')
    
    # Ejecutar el motor de reglas
    env.run()
    
    # Comprobar si los hechos generados cumplen con lo esperado
    resultados = [fact for fact in env.facts()]
    assert len(resultados) > 0  # Cambia esta condición según el test que hagas

if __name__ == "__main__":
    pytest.main()

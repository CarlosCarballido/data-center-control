import pytest
import clips
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la ruta de CLIPS desde la variable de entorno
clips_path = os.getenv("CLIPS_PATH")

def cargar_reglas_test():
    clips_env = clips.Environment()
    try:
        # Usar la ruta definida en la variable de entorno
        clips_env.load(f'{clips_path}/control_reglas.clp')
        print("Reglas cargadas correctamente.")
    except Exception as e:
        print(f"Error cargando control_reglas.clp: {e}")
    
    try:
        # Supone que 'hechos_test.clp' está en la carpeta 'tests'
        clips_env.load('tests/hechos_test.clp')
        print("Hechos iniciales cargados correctamente.")
    except Exception as e:
        print(f"Error cargando hechos_test.clp: {e}")
        
    clips_env.reset()
    
    print("\nHechos iniciales:")
    for fact in clips_env.facts():
        print(fact)
    
    return clips_env

def ejecutar_reglas_test(env):
    print("\nEjecutando reglas...")
    env.run()

    print("\nHechos generados:")
    for fact in env.facts():
        print(fact)

@pytest.fixture
def clips_env():
    # Configura el entorno de CLIPS cargando reglas y hechos iniciales
    env = cargar_reglas_test()
    return env

def test_verificar_ventiladores_altos(clips_env):
    # Insertar hecho de ventiladores con alto valor
    clips_env.assert_string('(actuadores (tipo ventiladores) (valor 500) (zona "Zona Alta"))')
    ejecutar_reglas_test(clips_env)
    assert any("Velocidad de los ventiladores alta" in str(fact) for fact in clips_env.facts())

def test_verificar_ventiladores_bajos(clips_env):
    # Insertar hecho de ventiladores con bajo valor
    clips_env.assert_string('(actuadores (tipo ventiladores) (valor 50) (zona "Zona Baja"))')
    ejecutar_reglas_test(clips_env)
    assert any("Velocidad de los ventiladores baja" in str(fact) for fact in clips_env.facts())

def test_verificar_temperatura(clips_env):
    # Insertar hecho de temperatura alta
    clips_env.assert_string('(sensor (tipo temperatura) (value 40) (zona "Zona Baja"))')
    ejecutar_reglas_test(clips_env)
    assert any("Temperatura alta en la zona" in str(fact) for fact in clips_env.facts())

def test_verificar_humedad(clips_env):
    # Insertar hecho de humedad alta
    clips_env.assert_string('(sensor (tipo humedad) (value 85) (zona "Zona Alta"))')
    ejecutar_reglas_test(clips_env)
    assert any("Humedad alta en la zona" in str(fact) for fact in clips_env.facts())

def test_verificar_luces_altas(clips_env):
    # Insertar hecho de luces con alto valor
    clips_env.assert_string('(actuadores (tipo luces) (valor 300) (zona "Zona Alta"))')
    ejecutar_reglas_test(clips_env)
    assert any("Las luces están muy brillantes" in str(fact) for fact in clips_env.facts())

def test_verificar_luces_bajas(clips_env):
    # Insertar hecho de luces con bajo valor
    clips_env.assert_string('(actuadores (tipo luces) (valor 5) (zona "Zona Baja"))')
    ejecutar_reglas_test(clips_env)
    assert any("Las luces están muy tenues" in str(fact) for fact in clips_env.facts())

def test_activar_alarma_incendio(clips_env):
    # Insertar sensor que detecta humo
    clips_env.assert_string('(sensor (tipo humo) (value si) (zona "Zona Alta"))')
    ejecutar_reglas_test(clips_env)
    assert any("Incendio detectado en la zona" in str(fact) for fact in clips_env.facts())

def test_activar_alarma_inundacion(clips_env):
    # Insertar sensor que detecta agua
    clips_env.assert_string('(sensor (tipo agua) (value si) (zona "Zona Baja"))')
    ejecutar_reglas_test(clips_env)
    assert any("Inundacion detectada en la zona" in str(fact) for fact in clips_env.facts())

if __name__ == 'main':
    pytest.main()
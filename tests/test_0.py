import clips
import pytest

from config import zonas

@pytest.fixture
def configurar_entorno():
    env = clips.Environment()

    env.load('clips/control_reglas.clp')

    # Inicialización mejorada para asegurar que no haya slots nil
    for nombre, atributos in zonas.items():
        env.assert_string(f'(zona (nombre "{nombre}") (temperatura {atributos.get("temperatura", 20)}) '
                          f'(humedad {atributos.get("humedad", 50)}) (estado_ac {atributos.get("estado_ac", "apagado")}) '
                          f'(acceso {atributos.get("acceso", "cerrado")}))')

    env.assert_string(f'(rack (id "Rack Baja") (voltaje 180))')
    env.assert_string(f'(actuadores (tipo ventiladores) (valor 450) (zona Zona_Alta))')
    env.assert_string(f'(actuadores (tipo ventiladores) (valor 150) (zona Zona_Baja))')
    env.assert_string(f'(actuadores (tipo luces) (valor 120) (zona Zona_Alta))')
    env.assert_string(f'(actuadores (tipo luces) (valor 10) (zona Zona_Baja))')
    env.assert_string(f'(sensor (tipo temperatura) (value 32) (zona Zona_Alta))')
    env.assert_string(f'(sensor (tipo temperatura) (value 18) (zona Zona_Baja))')
    env.assert_string(f'(sensor (tipo humedad) (value 80) (zona Zona_Alta))')
    env.assert_string(f'(sensor (tipo humedad) (value 50) (zona Zona_Baja))')
    env.assert_string(f'(sensor (tipo humo) (value si) (zona Zona_Alta))')
    env.assert_string(f'(sensor (tipo agua) (value no) (zona Zona_Baja))')

    return env, zonas

def test_activar_ac(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(sensor (tipo temperatura) (value 28) (zona "Zona_Alta"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(accion (tipo climatizacion) (comando "encender_ac")' in str(fact))

def test_apagar_ac(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(sensor (tipo temperatura) (value 20) (zona "Zona_Alta"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(accion (tipo climatizacion) (comando "apagar_ac")' in str(fact))

def test_activar_alarma_incendio(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(sensor (tipo humo) (value si) (zona "Zona_Alta"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(desastre (tipo incendio)' in str(fact))

def test_alerta_ventiladores_altos(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(actuadores (tipo ventiladores) (valor 500) (zona "Zona_Alta"))')
    env.run()
    print("=== Estado final de hechos ===")
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta ventiladores alta)' in str(fact))

def test_alerta_ventiladores_bajos(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(actuadores (tipo ventiladores) (valor 50) (zona "Zona_Baja"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta ventiladores baja)' in str(fact))

def test_alerta_voltaje_bajo(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(rack (id "Rack Baja") (voltaje 150))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta voltaje bajo)' in str(fact))

def test_alerta_humedad_alta(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(sensor (tipo humedad) (value 85) (zona "Zona_Alta"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta humedad alta)' in str(fact))

def test_alerta_temperatura_alta(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(sensor (tipo temperatura) (value 40) (zona "Zona_Baja"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta temperatura alta)' in str(fact))

def test_alerta_luces_altas(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(actuadores (tipo luces) (valor 300) (zona "Zona_Alta"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta luces alta)' in str(fact))

def test_alerta_luces_bajas(configurar_entorno):
    env, zonas = configurar_entorno
    env.assert_string('(actuadores (tipo luces) (valor 5) (zona "Zona_Baja"))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta luces baja)' in str(fact))

def test_alerta_acceso_abierto(configurar_entorno):
    env, zonas = configurar_entorno
    env.retract(env.find_fact("zona", lambda fact: fact.get_slot("nombre") == "Zona_Alta"))
    env.assert_string('(zona (nombre "Zona_Alta") (acceso abierto) (temperatura 20) (humedad 50) (estado_ac apagado))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta acceso abierto)' in str(fact))

def test_alerta_acceso_cerrado(configurar_entorno):
    env, zonas = configurar_entorno
    env.retract(env.find_fact("zona", lambda fact: fact.get_slot("nombre") == "Zona_Baja"))
    env.assert_string('(zona (nombre "Zona_Baja") (acceso cerrado) (temperatura 20) (humedad 50) (estado_ac encendido))')
    env.run()
    for fact in env.facts():
        print(fact)
    assert any(fact for fact in env.facts() if '(alerta acceso cerrado)' in str(fact))

if __name__ == "__main__":
    pytest.main()

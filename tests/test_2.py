import clips
import pytest

@pytest.fixture
def configurar_entorno():
    env = clips.Environment()

    env.load("clips/control_reglas.clp")

    # Establecer hechos iniciales para el entorno
    env.assert_string("(zona (nombre Zona_Alta) (temperatura 30) (humedad 60) (estado_ac apagado) (acceso abierto))")
    env.assert_string("(zona (nombre Zona_Baja) (temperatura 15) (humedad 40) (estado_ac encendido) (acceso cerrado))")
    env.assert_string("(sensor (tipo rack) (valor voltaje 180) (nombre Rack Baja))")
    env.assert_string("(actuadores (tipo ventiladores) (valor 450) (zona Zona_Alta))")
    env.assert_string("(actuadores (tipo ventiladores) (valor 150) (zona Zona_Baja))")
    env.assert_string("(actuadores (tipo luces) (valor 120) (zona Zona_Alta))")
    env.assert_string("(sensor (tipo temperatura) (value 18) (zona Zona_Alta))")
    env.assert_string("(sensor (tipo temperatura) (value 16) (zona Zona_Baja))")
    env.assert_string("(sensor (tipo humedad) (value 80) (zona Zona_Alta))")
    env.assert_string("(sensor (tipo humedad) (value 32) (zona Zona_Baja))")
    env.assert_string("(sensor (tipo humo) (value 50) (zona Zona_Alta))")
    env.assert_string("(sensor (tipo humo) (value 0) (zona Zona_Baja))")
    
    env.reset()

    return env

# Funciones auxiliares para mejorar la reutilización de código
def verificar_hecho(env, template_name, **conditions):
    """Verifica si existe un hecho que coincida con el template y las condiciones dadas."""
    for fact in env.facts():
        if fact.template.name == template_name and all(fact[slot] == value for slot, value in conditions.items()):
            return True
    return False

def test_activar_ac(configurar_entorno):
    env = configurar_entorno
    env.run()

    ac_encendido = verificar_hecho(env, "accion", comando="encender_ac", zona="Zona_Alta")
    assert ac_encendido, "El aire acondicionado debería haberse encendido en la Zona_Alta."

def test_activar_alarma_incendio(configurar_entorno):
    env = configurar_entorno
    env.run()

    alarma_incendio = verificar_hecho(env, "desastre", tipo="incendio", zona="Zona_Alta")
    assert alarma_incendio, "La alarma de incendio debería haberse activado en la Zona_Alta."

def test_alerta_ventiladores_altos(configurar_entorno):
    env = configurar_entorno
    env.run()

    alerta_ventiladores = verificar_hecho(env, "alerta", mensaje="Velocidad de los ventiladores alta")
    assert alerta_ventiladores, "Debería haber una alerta por ventiladores altos en la Zona_Alta."

def test_alerta_voltaje_bajo(configurar_entorno):
    env = configurar_entorno
    env.run()

    alerta_voltaje = verificar_hecho(env, "alerta", mensaje="Voltaje bajo en el rack")
    assert alerta_voltaje, "Debería haber una alerta de voltaje bajo en el Rack Baja."

if __name__ == "__main__":
    pytest.main()

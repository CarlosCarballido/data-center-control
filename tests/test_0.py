import clips
import pytest

@pytest.fixture
def configurar_entorno():
    env = clips.Environment()

    env.load('clips/control_reglas.clp')

    env.assert_string('(zona (nombre "Zona Alta") (temperatura 30) (humedad 60) (estado_ac apagado) (acceso abierto))')
    env.assert_string('(zona (nombre "Zona Baja") (temperatura 15) (humedad 40) (estado_ac encendido) (acceso cerrado))')
    env.assert_string('(rack (id "Rack Baja") (voltaje 180))')
    env.assert_string('(actuadores (tipo ventiladores) (valor 450) (zona "Zona Alta"))')
    env.assert_string('(actuadores (tipo ventiladores) (valor 150) (zona "Zona Baja"))')
    env.assert_string('(actuadores (tipo luces) (valor 120) (zona "Zona Alta"))')
    env.assert_string('(actuadores (tipo luces) (valor 10) (zona "Zona Baja"))')
    env.assert_string('(sensor (tipo temperatura) (value 32) (zona "Zona Alta"))')
    env.assert_string('(sensor (tipo temperatura) (value 18) (zona "Zona Baja"))')
    env.assert_string('(sensor (tipo humedad) (value 80) (zona "Zona Alta"))')
    env.assert_string('(sensor (tipo humedad) (value 50) (zona "Zona Baja"))')
    env.assert_string('(sensor (tipo humo) (value si) (zona "Zona Alta"))')
    env.assert_string('(sensor (tipo agua) (value no) (zona "Zona Baja"))')

    return env

def test_activar_ac(configurar_entorno):
    env = configurar_entorno
    env.run()

    ac_encendido = any(fact.template.name == "accion" and fact["comando"] == "encender_ac" and fact["nombre"] == "Zona Alta" for fact in env.facts())
    assert ac_encendido, "El aire acondicionado debería haberse encendido en la Zona Alta."

def test_activar_alarma_incendio(configurar_entorno):
    env = configurar_entorno
    env.run()

    alarma_incendio = any(fact.template.name == "desastre" and fact["tipo"] == "incendio" and fact["zona"] == "Zona Alta" for fact in env.facts())
    assert alarma_incendio, "La alarma de incendio debería haberse activado en la Zona Alta."

def test_alerta_ventiladores_altos(configurar_entorno):
    env = configurar_entorno
    env.run()

    alerta_ventiladores = any(fact.template.name == "fact-asserted" and "Velocidad de los ventiladores alta" in str(fact) for fact in env.facts())
    assert alerta_ventiladores, "Debería haber una alerta por ventiladores altos en la Zona Alta."

def test_alerta_voltaje_bajo(configurar_entorno):
    env = configurar_entorno
    env.run()

    alerta_voltaje = any("Voltaje bajo en el rack" in str(fact) for fact in env.facts())
    assert alerta_voltaje, "Debería haber una alerta de voltaje bajo en el Rack Baja."

if __name__ == "__main__":
    pytest.main()

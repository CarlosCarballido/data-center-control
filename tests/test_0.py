import clips
import pytest
from io import StringIO
import sys

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

def capturar_salida(env):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        env.run()
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def verificar_accion(env, comando, zona):
    salida = capturar_salida(env)
    accion = any(
        fact.template.name == "accion" and fact["comando"] == comando and fact["nombre"] == zona 
        for fact in env.facts()
    )
    assert accion, f"La acción '{comando}' debería haberse ejecutado en la {zona}."

def verificar_alerta(env, mensaje, zona):
    salida = capturar_salida(env)
    alerta_mensaje = mensaje.format(zona=zona)
    assert alerta_mensaje in salida, f"Debería haber una alerta: '{alerta_mensaje}'."

def verificar_desastre(env, tipo, zona):
    salida = capturar_salida(env)
    desastre = any(
        fact.template.name == "desastre" and fact["tipo"] == tipo and fact["zona"] == zona
        for fact in env.facts()
    )
    assert desastre, f"El desastre '{tipo}' debería haberse activado en la {zona}."

def test_activar_ac(configurar_entorno):
    env = configurar_entorno
    verificar_accion(env, "encender_ac", "Zona Alta")

def test_apagar_ac(configurar_entorno):
    env = configurar_entorno
    verificar_accion(env, "apagar_ac", "Zona Baja")

def test_activar_alarma_incendio(configurar_entorno):
    env = configurar_entorno
    verificar_desastre(env, "incendio", "Zona Alta")

def test_alerta_ventiladores_altos(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Velocidad de los ventiladores alta en la zona: {zona}", "Zona Alta")

def test_alerta_ventiladores_bajos(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Velocidad de los ventiladores baja en la zona: {zona}", "Zona Baja")

def test_alerta_voltaje_bajo(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Voltaje bajo en el rack: {zona}", "Rack Baja")

def test_alerta_humedad_alta(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Humedad alta en la zona: {zona}", "Zona Alta")

def test_alerta_temperatura_alta(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Temperatura alta en la zona: {zona}", "Zona Alta")

def test_alerta_luces_altas(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Las luces están muy brillantes en la zona: {zona}", "Zona Alta")

def test_alerta_luces_bajas(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Alerta: Las luces están muy tenues en la zona: {zona}", "Zona Baja")

def test_alerta_acceso_abierto(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Acceso abierto en la zona: {zona}", "Zona Alta")

def test_alerta_acceso_cerrado(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, "Acceso cerrado en la zona: {zona}", "Zona Baja")

if __name__ == "__main__":
    pytest.main()

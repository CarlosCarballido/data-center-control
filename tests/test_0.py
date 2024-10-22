import clips
import pytest
from io import StringIO
import sys

from config import zonas

@pytest.fixture
def configurar_entorno():
    env = clips.Environment()

    env.load('clips/control_reglas.clp')

    for nombre, atributos in zonas.items():
        env.assert_string(f'(zona (nombre "{nombre}") (temperatura {atributos["temperatura"]}) '
                          f'(humedad {atributos["humedad"]}) (estado_ac {atributos["estado_ac"]}) '
                          f'(acceso {atributos["acceso"]}))')

    env.assert_string(f'(rack (id "Rack Baja") (voltaje 180))')
    # Usa list() para convertir zonas.items() a una lista y accede al primer elemento
    env.assert_string(f'(actuadores (tipo ventiladores) (valor 450) (zona "{list(zonas.items())[0][0]}"))')
    env.assert_string(f'(actuadores (tipo ventiladores) (valor 150) (zona "{list(zonas.items())[1][0]}"))')
    env.assert_string(f'(actuadores (tipo luces) (valor 120) (zona "{list(zonas.items())[0][0]}"))')
    env.assert_string(f'(actuadores (tipo luces) (valor 10) (zona "{list(zonas.items())[1][0]}"))')
    env.assert_string(f'(sensor (tipo temperatura) (value 32) (zona "{list(zonas.items())[0][0]}"))')
    env.assert_string(f'(sensor (tipo temperatura) (value 18) (zona "{list(zonas.items())[1][0]}"))')
    env.assert_string(f'(sensor (tipo humedad) (value 80) (zona "{list(zonas.items())[0][0]}"))')
    env.assert_string(f'(sensor (tipo humedad) (value 50) (zona "{list(zonas.items())[1][0]}"))')
    env.assert_string(f'(sensor (tipo humo) (value si) (zona "{list(zonas.items())[0][0]}"))')
    env.assert_string(f'(sensor (tipo agua) (value no) (zona "{list(zonas.items())[1][0]}"))')

    return env, zonas


def capturar_salida(env):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        env.run()
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def verificar_accion(env, comando, zona):
    accion = any(
        fact.template.name == "accion" and fact["comando"] == comando and fact["nombre"] == zona 
        for fact in env.facts()
    )
    assert accion, f"La acción '{comando}' debería haberse ejecutado en la {zonas.items()[0][0]}."

def verificar_alerta(env, mensaje, zona):
    alerta_mensaje = mensaje.format(zona=zona)
    salida = capturar_salida(env)
    print(f"Verificando alerta: {alerta_mensaje}")
    print(f"Salida capturada: {salida}")
    assert alerta_mensaje in salida, f"Debería haber una alerta: '{alerta_mensaje}'."

def verificar_desastre(env, tipo, zona):
    desastre = any(
        fact.template.name == "desastre" and fact["tipo"] == tipo and fact["zona"] == zona
        for fact in env.facts()
    )
    assert desastre, f"El desastre '{tipo}' debería haberse activado en la {zonas.items()[0][0]}."

# Funciones de prueba actualizadas
def test_activar_ac(configurar_entorno):
    env = configurar_entorno
    verificar_accion(env, "encender_ac", f"{zonas.items()[0][0]}")

def test_apagar_ac(configurar_entorno):
    env = configurar_entorno
    verificar_accion(env, "apagar_ac", f"{zonas.items()[0][0]}")

def test_activar_alarma_incendio(configurar_entorno):
    env = configurar_entorno
    verificar_desastre(env, "incendio", f"{zonas.items()[0][0]}")

def test_alerta_ventiladores_altos(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Velocidad de los ventiladores alta en la zona: {zonas.items()[0][0]}", f"{zonas.items()[0][0]}")

def test_alerta_ventiladores_bajos(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Velocidad de los ventiladores baja en la zona: {zonas.items()[0][0]}", "Zona Baja")

def test_alerta_voltaje_bajo(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Voltaje bajo en el rack: {zonas.items()[0][0]}", "Rack Baja")

def test_alerta_humedad_alta(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Humedad alta en la zona: {zonas.items()[0][0]}", "{zonas.items())[0][0]}")

def test_alerta_temperatura_alta(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Temperatura alta en la zona: {zonas.items()[0][0]}", "{zonas.items())[0][0]}")

def test_alerta_luces_altas(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Las luces están muy brillantes en la zona: {zonas.items()[0][0]}", "{zonas.items())[0][0]}")

def test_alerta_luces_bajas(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Alerta: Las luces están muy tenues en la zona: {zonas.items()[0][0]}", "Zona Baja")

def test_alerta_acceso_abierto(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Acceso abierto en la zona: {zonas.items()[0][0]}", "{zonas.items())[0][0]}")

def test_alerta_acceso_cerrado(configurar_entorno):
    env = configurar_entorno
    verificar_alerta(env, f"Acceso cerrado en la zona: {zonas.items()[0][0]}", "Zona Baja")

if __name__ == "__main__":
    pytest.main()

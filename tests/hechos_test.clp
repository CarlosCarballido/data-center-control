;; hechos_test.clp

;; Hecho para test_alerta_ventiladores_altos
(actuadores (tipo ventiladores) (valor 500) (zona "Zona Alta"))

;; Hecho para test_alerta_ventiladores_bajos
(actuadores (tipo ventiladores) (valor 50) (zona "Zona Baja"))

;; Hecho para test_alerta_voltaje_bajo
(rack (id "Rack Baja") (voltaje 150))

;; Hecho para test_alerta_humedad_alta
(sensor (tipo humedad) (value 85) (zona "Zona Alta"))

;; Hecho para test_alerta_temperatura_alta
(sensor (tipo temperatura) (value 40) (zona "Zona Baja"))

;; Hecho para test_alerta_luces_altas
(actuadores (tipo luces) (valor 300) (zona "Zona Alta"))

;; Hecho para test_alerta_luces_bajas
(actuadores (tipo luces) (valor 5) (zona "Zona Baja"))

;; Hecho para test_alerta_acceso_abierto
(zona (nombre "Zona Alta") (acceso abierto) (temperatura 20) (humedad 50) (estado_ac apagado))

;; Hecho para test_alerta_acceso_cerrado
(zona (nombre "Zona Baja") (acceso cerrado) (temperatura 20) (humedad 50) (estado_ac encendido))

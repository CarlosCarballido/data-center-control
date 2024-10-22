;; Definiciones de hechos iniciales (deffacts)

(deffacts estado-inicial    
    ;; Zona con temperatura alta, humedad alta y acceso abierto
    (zona (nombre "Zona Alta") (temperatura 30) (humedad 60) (estado_ac apagado) (acceso abierto))
    
    ;; Zona con acceso cerrado y temperatura baja
    (zona (nombre "Zona Baja") (temperatura 15) (humedad 40) (estado_ac encendido) (acceso cerrado))

    ;; Rack con voltaje bajo
    (rack (id "Rack Baja") (voltaje 180))

    ;; Actuadores: Ventiladores y luces en distintas zonas
    (actuadores (tipo ventiladores) (valor 450) (zona "Zona Alta"))
    (actuadores (tipo ventiladores) (valor 150) (zona "Zona Baja"))
    (actuadores (tipo luces) (valor 120) (zona "Zona Alta"))
    (actuadores (tipo luces) (valor 10) (zona "Zona Baja"))

    ;; Sensores: Temperatura, humedad, humo y agua en distintas zonas
    (sensor (tipo temperatura) (value 32) (zona "Zona Alta"))
    (sensor (tipo temperatura) (value 18) (zona "Zona Baja"))
    (sensor (tipo humedad) (value 80) (zona "Zona Alta"))
    (sensor (tipo humedad) (value 50) (zona "Zona Baja"))
    (sensor (tipo humo) (value si) (zona "Zona Alta"))
    (sensor (tipo agua) (value no) (zona "Zona Baja"))
)

;; Definiciones de hechos iniciales (deffacts)

(deffacts estado-inicial    
    ;; Zona con temperatura alta, humedad aceptable y acceso cerrado
    (zona (nombre "Zona Alta") (temperatura 24) (humedad 60) (estado_ac apagado) (acceso cerrado))
    
    ;; Zona con acceso cerrado y temperatura baja
    (zona (nombre "Zona Baja") (temperatura 21) (humedad 40) (estado_ac apagado) (acceso cerrado))

    ;; Rack con voltaje adecuado
    (rack (id "Rack Baja") (voltaje 220))

    ;; Actuadores: Ventiladores y luces en distintas zonas
    (actuadores (tipo ventiladores) (valor 350) (zona "Zona Alta"))
    (actuadores (tipo ventiladores) (valor 250) (zona "Zona Baja"))
    (actuadores (tipo luces) (valor 82) (zona "Zona Alta"))
    (actuadores (tipo luces) (valor 30) (zona "Zona Baja"))

    ;; Sensores: Temperatura, humedad, humo y agua en distintas zonas
    (sensor (tipo temperatura) (value 24) (zona "Zona Alta"))
    (sensor (tipo temperatura) (value 23) (zona "Zona Baja"))
    (sensor (tipo humedad) (value 60) (zona "Zona Alta"))
    (sensor (tipo humedad) (value 40) (zona "Zona Baja"))
    (sensor (tipo humo) (value no) (zona "Zona Alta"))
    (sensor (tipo humo) (value no) (zona "Zona Baja"))
    (sensor (tipo agua) (value no) (zona "Zona Alta"))
    (sensor (tipo agua) (value no) (zona "Zona Baja"))
)

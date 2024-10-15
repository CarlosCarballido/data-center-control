;; Definiciones de hechos iniciales (deffacts)

(deffacts estado-inicial    
    ;; Zona con temperatura alta, humedad alta y acceso abierto
    (zona (nombre "Zona Alta") (temperatura 30) (humedad 60) (estado_ac apagado) (acceso abierto))
    
    ;; Zona con acceso cerrado y temperatura baja
    (zona (nombre "Zona Baja") (temperatura 15) (humedad 40) (estado_ac encendido) (acceso cerrado))

    ;; Rack con voltaje bajo
    (rack (id "Rack Baja") (voltaje 180))
)

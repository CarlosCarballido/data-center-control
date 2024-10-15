;; Definiciones de hechos iniciales (deffacts)

(deffacts estado-inicial
    ;; Zona 1
    (zona (nombre "Zona 1") (temperatura 27) (humedad 40) (estado_ac apagado))
    
    ;; Zona 2
    (zona (nombre "Zona 2") (temperatura 19) (humedad 50) (estado_ac encendido))
    
    ;; Rack 1 en Zona 1
    (rack (id "Rack 1") (voltaje 220))

    ;; Rack 2 en Zona 2
    (rack (id "Rack 2") (voltaje 200)) ;; Voltaje bajo para disparar alerta
)

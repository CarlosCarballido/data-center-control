;; Definiciones de hechos iniciales (deffacts)

(deffacts estado-inicial
    ;; Zona con temperatura alta para activar el AC
    (zona (nombre "Zona Alta") (temperatura 30) (humedad 50) (estado_ac apagado))
    
    ;; Rack con voltaje bajo
    (rack (id "Rack Baja") (voltaje 180))
)
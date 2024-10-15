;; Definición de plantillas de hechos (deftemplate)
(deftemplate zona
    (slot nombre)
    (slot temperatura)
    (slot humedad)
    (slot estado_ac) ;; encendido, apagado
)

(deftemplate rack
    (slot id)
    (slot voltaje)
)

(deftemplate accion
    (slot tipo)    ;; climatizacion, desastre, etc.
    (slot comando) ;; encender_ac, apagar_ac, etc.
    (slot nombre)  ;; nombre de la zona
)

;; Reglas de control (defrule)

;; Regla para encender el aire acondicionado si la temperatura es mayor a 25°C
(defrule encender-ac
    (zona (nombre ?nombre) (temperatura ?temp&:(> ?temp 25)))
    =>
    (assert (accion (tipo climatizacion) (comando "encender_ac")))
    (printout t "Encendiendo aire acondicionado en la zona: " ?nombre crlf)
)

(defrule apagar-ac
    (zona (nombre ?nombre) (temperatura ?temp&:(<= ?temp 20)))
    =>
    (assert (accion (tipo climatizacion) (comando "apagar_ac")))
    (printout t "Apagando aire acondicionado en la zona: " ?nombre crlf)
)


;; Regla para emitir alerta si el voltaje de un rack es inferior a 210V
(defrule alerta-voltaje
    (rack (id ?id) (voltaje ?v&:(< ?v 210)))
    =>
    (printout t "Alerta: Voltaje bajo en el rack: " ?id crlf)
)

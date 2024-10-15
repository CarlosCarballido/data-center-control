(deftemplate zona
    (slot nombre)
    (slot temperatura)
    (slot humedad)
    (slot estado_ac) ;; encendido, apagado
    (slot acceso)    ;; abierto, cerrado
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

(defrule encender-ac
    (zona (nombre ?nombre) (temperatura ?temp&:(> ?temp 25)))
    =>
    (assert (accion (tipo climatizacion) (comando "encender_ac") (nombre ?nombre)))
    (printout t "Encendiendo aire acondicionado en la zona: " ?nombre crlf)
)

(defrule apagar-ac
    (zona (nombre ?nombre) (temperatura ?temp&:(<= ?temp 20)))
    =>
    (assert (accion (tipo climatizacion) (comando "apagar_ac") (nombre ?nombre)))
    (printout t "Apagando aire acondicionado en la zona: " ?nombre crlf)
)

(defrule alerta-voltaje
    (rack (id ?id) (voltaje ?v&:(< ?v 210)))
    =>
    (printout t "Alerta: Voltaje bajo en el rack: " ?id crlf)
)

(defrule alerta-humedad
    (zona (nombre ?nombre) (humedad ?h&:(> ?h 70)))
    =>
    (printout t "Alerta: Humedad alta en la zona: " ?nombre crlf)
)

(defrule verificar-acceso
    (zona (nombre ?nombre) (acceso abierto))
    =>
    (printout t "Acceso abierto en la zona: " ?nombre crlf)
)

(defrule verificar-acceso-cerrado
    (zona (nombre ?nombre) (acceso cerrado))
    =>
    (printout t "Acceso cerrado en la zona: " ?nombre crlf)
)
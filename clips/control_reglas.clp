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

(deftemplate desastre
    (slot tipo)    ;; incendio, inundacion, etc.
    (slot zona)    ;; nombre de la zona
)

(deftemplate sensor
    (slot tipo)    ;; temperatura, humedad, etc.
    (slot valor)
)

(deftemplate actuadores
    (slot zona)
    (slot tipo)    ;; ventiladores, luces, altavoces etc.
    (slot valor)
)

(deftemplate humo
    (slot zona)
)

(deftemplate agua
    (slot zona)
)

(deftemplate sensor
    (slot tipo)    ;; temperatura, humedad, etc.
    (slot value)
    (slot zona)
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

(defrule verificar-temperatura
    (sensor (tipo temperatura) (value ?temp&:(> ?temp 25)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (printout t "Alerta: Temperatura alta en la zona: " ?zona crlf)
)

(defrule verificar-humedad
    (sensor (tipo humedad) (value ?h&:(> ?h 70)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (printout t "Alerta: Humedad alta en la zona: " ?zona crlf)
)

(defrule verificar-ventiladores-altos
    (actuadores (tipo ventiladores) (valor ?v&:(> ?v 400)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (printout t "Alerta: Velocidad de los ventiladores alta en la zona: " ?zona crlf)
)

(defrule verificar-ventiladores-bajos
    (actuadores (tipo ventiladores) (valor ?v&:(< ?v 200)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (printout t "Alerta: Velocidad de los ventiladores baja en la zona: " ?zona crlf)
)

(defrule verificar-luces-altas
    (actuadores (tipo luces) (valor ?l&:(> ?l 100)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (printout t "Alerta: Las luces están muy brillantes en la zona: " ?zona crlf)
)

(defrule verificar-luces-bajas
    (actuadores (tipo luces) (valor ?l&:(< ?l 20)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (printout t "Alerta: Las luces están muy tenues en la zona: " ?zona crlf)
)


(defrule activar-alarma-incendio
    (sensor (tipo humo) (value si) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (desastre (tipo incendio) (zona ?zona)))
    (printout t "Alerta: Incendio detectado en la zona: " ?zona crlf)
)

(defrule activar-alarma-inundacion
    (sensor (tipo agua) (value si) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (desastre (tipo inundacion) (zona ?zona)))
    (printout t "Alerta: Inundacion detectada en la zona: " ?zona crlf)
)

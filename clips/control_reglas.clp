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
    (slot tipo)    ;; ventiladores, luces, altavoces etc.
    (slot valor)
)

(deftemplate humo
    (slot zona)
)

(deftemplate agua
    (slot zona)
)

(deftemplate sensor_humo
    (slot value)
    (slot zona)
)

(deftemplate sensor_agua
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
    (temperature_sensor (value ?temp&:(> ?temp 25)) (zona (nombre ?nombre)))
    =>
    (printout t "Alerta: Temperatura alta en el sensor de temperatura en la zona: " ?nombre crlf)
)

(defrule verificar-humedad
    (humidity_sensor (value ?h&:(> ?h 70)) (zona (nombre ?nombre)))
    =>
    (printout t "Alerta: Humedad alta en el sensor de humedad en la zona: " ?nombre crlf)
)

(defrule verificar-fans
    (fans (value ?v&:(> ?v 400)) (zona (nombre ?nombre)))
    =>
    (printout t "Alerta: Velocidad de los ventiladores alta en la zona: " ?nombre crlf)
)

(defrule verificar-fans-bajos
    (fans (value ?v&:(< ?v 200)) (zona (nombre ?nombre)))
    =>
    (printout t "Alerta: Velocidad de los ventiladores baja en la zona: " ?nombre crlf)
)

(defrule activar-alarma-incendio
    (smoke_sensor (value si) (zona (nombre ?nombre)))
    =>
    (assert (desastre (tipo incendio) (zona (nombre ?nombre))))
    (printout t "Alerta: Incendio detectado en la zona: " ?nombre crlf)
)

(defrule activar-alarma-inundacion
    (water_sensor (value si) (zona (nombre ?nombre)))
    =>
    (assert (desastre (tipo inundacion) (zona ?nombre)))
    (printout t "Alerta: Inundacion detectada en la zona: " ?nombre crlf)
)

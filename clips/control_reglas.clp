(deftemplate zona
    (slot nombre)
    (slot temperatura)
    (slot humedad)
    (slot estado_ac) ;; encendido, apagado
    (slot acceso)    ;; abierto, cerrado
    (slot nivel_acceso) ;; 1, 2, 3 - nivel de acceso requerido
)

(deftemplate usuario
    (slot nombre)
    (slot rango) ;; 1 = menor acceso, 3 = mayor acceso
)

(deftemplate rack
    (slot id)
    (slot voltaje)
)

(deftemplate accion
    (slot tipo)    ;; climatizacion, desastre, etc.
    (slot comando) ;; encender_ac, apagar_ac, etc.
    (slot nombre)  ;; nombre de la zona
    (slot resuelta (default FALSE))  ;; indica si la alerta ya ha sido gestionada
    (slot nivel_acceso) ;; nivel de acceso necesario para ejecutar la acción
)

(deftemplate desastre
    (slot tipo)    ;; incendio, inundacion, etc.
    (slot zona)    ;; nombre de la zona
)

(deftemplate sensor
    (slot tipo)    ;; temperatura, humedad, etc.
    (slot value)
    (slot zona)
)

(deftemplate actuadores
    (slot zona)
    (slot tipo)    ;; ventiladores, luces, altavoces etc.
    (slot valor)
)

;; Reglas para climatización

(defrule encender-ac
    (zona (nombre ?nombre) (temperatura ?temp&:(> ?temp 25)))
    =>
    (printout t "Encendiendo aire acondicionado en la zona " ?nombre "." crlf)
)

(defrule apagar-ac
    (zona (nombre ?nombre) (temperatura ?temp&:(< ?temp 18)))
    =>
    (printout t "Apagando aire acondicionado en la zona " ?nombre "." crlf)
)

;; Reglas de alertas para monitoreo

(defrule alerta-voltaje
    (rack (id ?id) (voltaje ?v&:(< ?v 210)))
    =>
    (assert (accion (tipo alerta) (comando "voltaje_bajo") (nombre ?id)))
    (printout t "Alerta: Voltaje bajo en el rack: " ?id crlf)
)

(defrule alerta-humedad
    (zona (nombre ?nombre) (humedad ?h&:(> ?h 70)))
    =>
    (assert (accion (tipo alerta) (comando "humedad_alta") (nombre ?nombre)))
    (printout t "Alerta: Humedad alta en la zona: " ?nombre crlf)
)

;; Reglas para verificar acceso

(defrule verificar-acceso
    (zona (nombre ?nombre) (acceso abierto))
    =>
    (assert (accion (tipo informacion) (comando "acceso_abierto") (nombre ?nombre)))
    (printout t "Acceso abierto en la zona: " ?nombre crlf)
)

(defrule verificar-acceso-cerrado
    (zona (nombre ?nombre) (acceso cerrado))
    =>
    (assert (accion (tipo informacion) (comando "acceso_cerrado") (nombre ?nombre)))
    (printout t "Acceso cerrado en la zona: " ?nombre crlf)
)

;; Reglas para sensores

(defrule verificar-temperatura
    (sensor (tipo temperatura) (value ?temp&:(> ?temp 25)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "temperatura_alta") (nombre ?zona)))
    (printout t "Alerta: Temperatura alta en la zona: " ?zona crlf)
)

(defrule verificar-humedad
    (sensor (tipo humedad) (value ?h&:(> ?h 70)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "humedad_alta") (nombre ?zona)))
    (printout t "Alerta: Humedad alta en la zona: " ?zona crlf)
)

;; Reglas para actuadores

(defrule verificar-ventiladores-altos
    (actuadores (tipo ventiladores) (valor ?v&:(> ?v 400)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "ventiladores_altos") (nombre ?zona)))
    (printout t "Alerta: Velocidad de los ventiladores alta en la zona: " ?zona crlf)
)

(defrule verificar-ventiladores-bajos
    (actuadores (tipo ventiladores) (valor ?v&:(< ?v 200)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "ventiladores_bajos") (nombre ?zona)))
    (printout t "Alerta: Velocidad de los ventiladores baja en la zona: " ?zona crlf)
)

(defrule verificar-luces-altas
    (actuadores (tipo luces) (valor ?l&:(> ?l 100)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "luces_altas") (nombre ?zona)))
    (printout t "Alerta: Las luces están muy brillantes en la zona: " ?zona crlf)
)

(defrule verificar-luces-bajas
    (actuadores (tipo luces) (valor ?l&:(< ?l 20)) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "luces_bajas") (nombre ?zona)))
    (printout t "Alerta: Las luces están muy tenues en la zona: " ?zona crlf)
)

;; Reglas para desastres

(defrule activar-alarma-incendio
    (sensor (tipo humo) (value si) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "incendio_detectado") (nombre ?zona)))
    (printout t "Alerta: Incendio detectado en la zona: " ?zona crlf)
)

(defrule activar-alarma-inundacion
    (sensor (tipo agua) (value si) (zona ?zona))
    (zona (nombre ?zona))
    =>
    (assert (accion (tipo alerta) (comando "inundacion_detectada") (nombre ?zona)))
    (printout t "Alerta: Inundacion detectada en la zona: " ?zona crlf)
)

(defrule acceso-zona-restringido
    (usuario (nombre ?usuario) (rango ?rango&:(integer ?rango)))
    (zona (nombre ?nombre) (nivel_acceso ?nivel_acceso&:(integer ?nivel_acceso)))
    =>
    (bind ?mayor_acceso (> ?nivel_acceso ?rango))
    (if ?mayor_acceso then
        (printout t "Acceso denegado para el usuario " ?usuario " a la zona " ?nombre " debido a rango insuficiente." crlf)
    )
)

;; Regla para permitir acceso a usuarios con nivel suficiente

(defrule acceso-zona
    (usuario (nombre ?usuario) (rango ?rango&:(integer ?rango)))
    (zona (nombre ?nombre) (nivel_acceso ?nivel_acceso&:(integer ?nivel_acceso)))
    =>
    (bind ?permitido (<= ?nivel_acceso ?rango))
    (if ?permitido then
        (printout t "Acceso permitido para el usuario " ?usuario " a la zona " ?nombre "." crlf)
    )
)
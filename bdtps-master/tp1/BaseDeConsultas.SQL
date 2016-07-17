#Veo los articulos que compro un usuario
select 	a.nombre, a.precio
from 	usuario u, compra c, articulo a 
where 	u.idUsuario = <INSERTE ID USUARIO A BUSCAR> ^
		u.idUsuario = c.idUsuario ^
		c.idPublicacion = a.idPublicacion

#Veo los articulos que vendio el usuario
select 	a.nombre, a.precio
from 	usuario u, articulo a, publicacion p
where 	p.idUsuarioCreador = <INSERTE ID USUARIO A BUSCAR> ^
		p.idPublicacion IN (	select c.idPublicacion
								from compra c) ^
		p.idPublicacion = a.idPublicacion

#Veo los articulos que fueron visitas (y cuando fueron visitados)
select	a.nombre, v.timestamp
from 	visita v, articulo a 
where 	v.idUsuario = <INSERTE ID USUARIO A BUSCAR> ^
		v.idPublicacion = a.idPublicacion

#No tenemos favoritos para hacer favoritos



#Intente usar una acumulacion con un count(*), pero no podemos usarlo dentro del where
#El tema es que hay que pedir que sea mayor que todos los demas. No me termina de cerrar.

#El cuatri pasado hice algo parecido, voy a ver si t

#select 	a1.nombre, a2.nombre, a3.nombre
#from 	articulo a1, articulo a2, articulo a3, usuario u, publicacion v1, publicacion v2, publicacion v3
#where 	u.idUsuario = <INSERTE ID USUARIO A BUSCAR>
	#	(	select		count(*)
	#		from		visita v
	#		where		v.idUsuario = u.idUsuario
	#		group by	v.idPublicacion
		#)
import sqlite3
import time
import datetime


con = sqlite3.connect('BaseRelacional.db')
c = con.cursor()

#p.idUsuarioCreador as idUsuario, sum(a.precio) as ventas, strftime('%Y-%m',c.timestamp) as fecha, GROUP_CONCAT ( '<' || p.titulo || ',' || a.precio || ',' || (a.precio * tp.comision / 100) || '>')  as compra"""

queryReputacion = """
Select p.idUsuarioCreador as idUsuario, avg(e.calificacion) as reputacion

FROM

COMPRA c,

PUBLICACION p,

EVALUACION e

WhERE

c.idCompra = e.idCompra AND

c.idPublicacion = p.idPublicacion

GROUP BY p.idUsuarioCreador

"""

queryVentas = """
SELECT c.idCompra, c.timestamp, c.cantidadCuotas, 

'<' || u2.idUsuario || ',' || '[' || u2.localidad || ',' || u2.calle || ',' || u2.numero || ']' || ',' || case when r2.reputacion is null then 'None' else r2.reputacion end|| '>',


'<' || u1.idUsuario || ',' || case when  u1.inscripcionesRubi is not null then 1 else 0 end || ',' || case when r1.reputacion is null then 'None' else r1.reputacion end || '>' as vendedor,

a.precio,

a.precio * tp.comision / 100

FROM 

PUBLICACION p 

INNER JOIN TIPO_DE_PUBLICACION tp on p.nombreTipo = tp.nombre 

INNER JOIN ARTICULO a on p.idPublicacion = a.idPublicacion

INNER JOIN COMPRA c on p.idPublicacion = c.idPublicacion

INNER JOIN USUARIO u1 on p.idUsuarioCreador = u1.idUsuario

INNER JOIN USUARIO u2 on c.idUsuario = u2.idUsuario

LEFT OUTER JOIN ("""+ queryReputacion +""") r1 on u1.idUsuario = r1.idUsuario

LEFT OUTER JOIN ("""+ queryReputacion +""") r2 on u2.idUsuario = r2.idUsuario

"""

c.execute(queryVentas)
result = c.fetchall()

for x in result:   
    print(x)
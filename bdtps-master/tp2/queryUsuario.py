import sqlite3
import time
import datetime


con = sqlite3.connect('BaseRelacional.db')
c = con.cursor()


queryDatosDeUsuario = """
SELECT p.idUsuarioCreador as idUsuario,  '<' || u.localidad || ',' || u.calle || ',' || u.numero || '>' as domicilio

FROM 

PUBLICACION p 

INNER JOIN COMPRA c on p.idPublicacion = c.idPublicacion

INNER JOIN USUARIO u on p.idUsuarioCreador = u.idUsuario

"""

queryVentasSeparadasPorMes = """
SELECT p.idUsuarioCreador as idUsuario, sum(a.precio) as ventas, strftime('%Y-%m',c.timestamp) as fecha, GROUP_CONCAT ( '<' || p.titulo || ',' || a.precio || ',' || (a.precio * tp.comision / 100) || '>')  as compra

FROM 

PUBLICACION p 

INNER JOIN TIPO_DE_PUBLICACION tp on p.nombreTipo = tp.nombre 

INNER JOIN ARTICULO a on p.idPublicacion = a.idPublicacion

INNER JOIN COMPRA c on p.idPublicacion = c.idPublicacion

Group by p.idUsuarioCreador, strftime('%m', c.timestamp)

"""

queryDatosComoVendedor = """
SELECT q.idUsuario as idUsuario, sum(q.ventas) as totalVendido, GROUP_CONCAT(q.fecha  || '[' || q.compra || ']') as ventas from ("""+queryVentasSeparadasPorMes+""") q 

Group by q.idUsuario
"""

queryUsuario = """
SELECT vn.idUsuario, vn.domicilio, vxm.totalVendido, vxm.ventas FROM  (""" + queryDatosDeUsuario + """) vn,  ("""+ queryDatosComoVendedor +""") vxm  

where

vn.idUsuario = vxm.idUsuario
"""


c.execute(queryUsuario)
result = c.fetchall()

for x in result:   
    print(x)
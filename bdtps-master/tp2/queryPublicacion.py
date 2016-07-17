import sqlite3
import time
import datetime


con = sqlite3.connect('BaseRelacional.db')
c = con.cursor()

#p.idUsuarioCreador as idUsuario, sum(a.precio) as ventas, strftime('%Y-%m',c.timestamp) as fecha, GROUP_CONCAT ( '<' || p.titulo || ',' || a.precio || ',' || (a.precio * tp.comision / 100) || '>')  as compra"""

queryPublicacion = """
Select p.idPublicacion, a.idArticulo, s.idServicio

FROM

PUBLICACION p

LEFT OUTER JOIN ARTICULO a ON a.idPublicacion = p.idPublicacion

LEFT OUTER JOIN SERVICIO s ON p.idPublicacion = s.idPublicacion
"""

c.execute(queryPublicacion)
result = c.fetchall()

for x in result:   
    print(x)
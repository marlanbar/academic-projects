--Consulta por categoría de producto: obtener, dada una categoría de producto (“Computación”,
--“Hogar, muebles y jardín”, etc), un listado de los vendedores que han publicado artículos de dicha
--categoría y la cantidad de ventas que efectuó cada uno de dichos vendedores.

SELECT P.[idUsuarioCreador] AS Usuario, COUNT(C.[idCompra]) AS 'Cantidad de ventas'
FROM PUBLICACION AS P 
     INNER JOIN COMPRA AS C ON P.[idPublicacion] = C.[idPublicacion] 
WHERE C.[idUsuario] IN (
  SELECT DISTINCT P2.idUsuarioCreador
  FROM PUBLICACION AS P2
  WHERE P2.[nombreCategoria] = 'Hogar'  
)
GROUP BY P.[idUsuarioCreador]

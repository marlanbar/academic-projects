--Consulta por categor�a de producto: obtener, dada una categor�a de producto (�Computaci�n�,
--�Hogar, muebles y jard�n�, etc), un listado de los vendedores que han publicado art�culos de dicha
--categor�a y la cantidad de ventas que efectu� cada uno de dichos vendedores.

SELECT P.[idUsuarioCreador] AS Usuario, COUNT(C.[idCompra]) AS 'Cantidad de ventas'
FROM PUBLICACION AS P 
     INNER JOIN COMPRA AS C ON P.[idPublicacion] = C.[idPublicacion] 
WHERE C.[idUsuario] IN (
  SELECT DISTINCT P2.idUsuarioCreador
  FROM PUBLICACION AS P2
  WHERE P2.[nombreCategoria] = 'Hogar'  
)
GROUP BY P.[idUsuarioCreador]

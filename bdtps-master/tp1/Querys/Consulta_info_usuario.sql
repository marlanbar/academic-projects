--Consulta por usuario: obtener, para un usuario específico, información sobre los artículos que ha
--comprado y vendido, los artículos que ha visitado con su fecha de visita, los artículos que tiene
--en su lista de favoritos.

SELECT * FROM (

SELECT 'Compra' AS 'Accion', A.[nombre] as Nombre, A.[precio] as Precio, C.[timestamp] AS Fecha
FROM COMPRA AS C 
     INNER JOIN PUBLICACION AS P ON C.[idPublicacion] = P.[idPublicacion]     
     INNER JOIN ARTICULO AS A ON P.[idPublicacion] = A.[idPublicacion]
WHERE C.[idUsuario] = 'pepito'

UNION ALL

SELECT 'Venta' AS 'Accion', A.[nombre] as Nombre, A.[precio] as Precio, C.[timestamp] AS Fecha
FROM COMPRA AS C 
     INNER JOIN PUBLICACION AS P ON C.[idPublicacion] = P.[idPublicacion]     
     INNER JOIN ARTICULO AS A ON P.[idPublicacion] = A.[idPublicacion]
WHERE P.[idUsuarioCreador] = 'pepito'

UNION ALL

SELECT 'Visita' AS 'Accion', A.[nombre] as Nombre, A.[precio] as Precio, V.[timestamp] AS Fecha
FROM VISITA AS V 
     INNER JOIN PUBLICACION AS P ON V.[idPublicacion] = P.[idPublicacion]     
     INNER JOIN ARTICULO AS A ON P.[idPublicacion] = A.[idPublicacion]
WHERE V.[idUsuario] = 'pepito'

UNION ALL

SELECT 'Favorito' AS 'Accion', A.[nombre] as Nombre, A.[precio] as Precio, NULL AS Fecha
FROM SIGUE AS S 
     INNER JOIN PUBLICACION AS P ON S.[idPublicacion] = P.[idPublicacion]     
     INNER JOIN ARTICULO AS A ON P.[idPublicacion] = A.[idPublicacion]
WHERE S.[idUsuario] = 'pepito'


)

ORDER BY Fecha 


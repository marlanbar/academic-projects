--Consulta por usuario: obtener, para un usuario espec�fico, informaci�n sobre los art�culos que ha
--comprado y vendido, los art�culos que ha visitado con su fecha de visita, los art�culos que tiene
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


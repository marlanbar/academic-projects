--Consulta por usuario: obtener, para un usuario espec�fico, las primeras 3 categor�as 
--de art�culos que visit� con mayor frecuencia en el �ltimo a�o.

SELECT P.nombreCategoria AS Categoria, COUNT(P.nombreCategoria) AS Visitas
FROM VISITA AS V
     INNER JOIN PUBLICACION AS P ON V.[idPublicacion] = P.[idPublicacion]  
WHERE V.[idUsuario] = 'pepito' AND strftime('%Y', timestamp) = strftime('%Y', CURRENT_DATE)
GROUP BY P.nombreCategoria
ORDER BY Visitas DESC LIMIT 3

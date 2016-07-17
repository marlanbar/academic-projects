--Consulta por usuario: obtener, para un usuario específico, las primeras 3 categorías 
--de artículos que visitó con mayor frecuencia en el último año.

SELECT P.nombreCategoria AS Categoria, COUNT(P.nombreCategoria) AS Visitas
FROM VISITA AS V
     INNER JOIN PUBLICACION AS P ON V.[idPublicacion] = P.[idPublicacion]  
WHERE V.[idUsuario] = 'pepito' AND strftime('%Y', timestamp) = strftime('%Y', CURRENT_DATE)
GROUP BY P.nombreCategoria
ORDER BY Visitas DESC LIMIT 3

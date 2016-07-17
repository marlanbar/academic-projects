--Consulta por ganador/es anual de viaje a Khan El-Khalili: obtener, para un año específico, el
--ganador/es.

SELECT idUsuario, SUM(Monto) AS Total FROM (

  SELECT C.[idUsuario], COALESCE(SUM(A.precio), 0) + COALESCE(SUM(S.[precioPorHora] * S.[cantidadDeHoras]), 0) AS Monto 
  FROM COMPRA AS C
       INNER JOIN PUBLICACION AS P ON P.[idPublicacion] = C.[idPublicacion]
       LEFT JOIN ARTICULO AS A ON A.[idPublicacion] = P.[idPublicacion]
       LEFT JOIN SERVICIO AS S ON S.[idPublicacion] = P.[idPublicacion]     
  WHERE strftime('%Y', C.[timestamp]) = '2016'
  GROUP BY C.[idUsuario]
  
  UNION ALL
  
  SELECT O.[idUsuario], COALESCE(SUM(O.monto), 0) AS Monto
  FROM OFERTA AS O
       INNER JOIN PUBLICACION AS P ON P.[idPublicacion] = O.[idPublicacion]
  WHERE P.[estaVigente] = 0 AND strftime('%Y', O.[timestamp]) = 2016 AND
        O.[timestamp] = ( 
        SELECT MAX(O2.timestamp)    
        FROM OFERTA AS O2     
        WHERE O2.[idPublicacion] = P.[idPublicacion]
              AND strftime('%Y', O2.[timestamp]) = '2016'      
  )
  GROUP BY O.[idUsuario]
)
GROUP BY idUsuario
ORDER BY Total DESC
LIMIT 1


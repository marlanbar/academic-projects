--Consulta por usuario y preguntas: obtener para un usuario específico, la lista de preguntas que
--ha realizado, con las respectivas respuestas que haya recibido (sólo la pregunta, si aún no recibió
--respuesta).

SELECT P.texto AS Pregunta, R.texto AS Respuesta
FROM PREGUNTA AS P LEFT JOIN RESPUESTA AS R ON P.idPregunta = R.idPregunta
WHERE idUsuario = ?

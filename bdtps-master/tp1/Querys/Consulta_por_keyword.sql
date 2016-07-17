--Consulta por keyword: obtener, para un cierto keyword (por ejemplo “mesa”), la lista de publicaciones
--vigentes que tengan en el título, dicha keyword. El usuario debe poder restringir su
--búsqueda sólo a cierta categoría de artículos o servicios.

SELECT idPublicacion, titulo
FROM PUBLICACION
WHERE titulo LIKE '%escoba%' AND nombreCategoria = ? -- ej: Hogar


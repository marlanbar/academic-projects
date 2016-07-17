CREATE DEFINER=`root`@`localhost` PROCEDURE `HistorialLicenciaConTriggers`(nrolicencia int )
BEGIN

select S.Fecha, Lugar.Direccion, TA.Descipcion as TipoAccidente, Participante.TipoParticipacion as Participacion
from licencia L
inner join Conductor C on L.nroLicencia = C.nroLicencia
inner join Persona P on C.dni = P.dni
/*Filtrar por Dni*/
inner join Participante on Participante.dni = P.dni
inner join Siniestro S on S.idSiniestro = Participante.idSiniestro
inner join Lugar on Lugar.idLugar = S.idLugar
inner join TipoAccidente TA on TA.idTipoAccidente = S.idTipoAccidente
where L.nroLicencia = nrolicencia;

/*También se deberá indicar la cantidad de automóviles que está habilitado a conducir*/
SELECT 
    V.Dominio,
    V.FechaPatentamiento,
    C.Descripcion AS Categoria,
    TV.Descripcion AS TipoVehiculo
FROM
    Licencia L
        INNER JOIN
    Conductor ON L.nroLicencia = Conductor.nroLicencia
        INNER JOIN
    conductorhabilitado CH ON CH.DNI = Conductor.dni
        INNER JOIN
    vehiculo V ON V.idVehiculo = CH.idVehiculo
        INNER JOIN
    Categoria C ON C.idCategoria = V.IdCategoria
        INNER JOIN
    TipoVehiculo TV ON TV.idTipoVehiculo = V.idTipoVehiculo
WHERE
    L.nroLicencia = nrolicencia;
END
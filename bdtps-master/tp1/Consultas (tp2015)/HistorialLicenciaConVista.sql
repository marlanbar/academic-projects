CREATE DEFINER=`root`@`localhost` PROCEDURE `HistorialLicenciaConVista`(nrolicencia int )
BEGIN

select S.Fecha, Lugar.Direccion, TA.Descipcion as TipoAccidente, Participantes.Participacion
from licencia L
inner join Conductor C on L.nroLicencia = C.nroLicencia
inner join Persona P on C.dni = P.dni
/*Filtrar por Dni*/
inner join Participantes on Participantes.dni = P.dni
inner join Siniestro S on S.idSiniestro = Participantes.idSiniestro
inner join Lugar on Lugar.idLugar = S.idLugar
inner join TipoAccidente TA on TA.idTipoAccidente = S.idTipoAccidente
where L.nroLicencia = nrolicencia;

/*También se deberá indicar la cantidad de automóviles que está habilitado a conducir*/
/*Detalle de los automoviles Habiltados*/
select V.Dominio, V.FechaPatentamiento, C.Descripcion as Categoria, TV.Descripcion as TipoVehiculo
from Licencia L 
inner join Conductor on L.nroLicencia = Conductor.nroLicencia
inner join conductorhabilitado CH on CH.DNI = Conductor.dni 
inner join vehiculo V on V.idVehiculo = CH.idVehiculo
inner join Categoria C on C.idCategoria =V.IdCategoria
inner join TipoVehiculo TV on TV.idTipoVehiculo = V.idTipoVehiculo
where L.nroLicencia = nrolicencia;
END
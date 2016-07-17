USE `tp1`;
DROP procedure IF EXISTS `HistorialLicencia`;

DELIMITER $$
USE `tp1`$$
/*Consulta por número de licencia: obtener, con un número de licencia específico,
información sobre los accidentes en los que ha participado el conductor propietario de
la misma, con detalles de fecha, lugar, tipo de accidente, participación y modalidad.
También se deberá indicar la cantidad de automóviles que está habilitado a conducir*/
CREATE PROCEDURE `HistorialLicencia` (nrolicencia int )
BEGIN

select S.Fecha, Lugar.Direccion, TA.Descipcion as TipoAccidente, Participacion.Participacion
from licencia L
inner join Conductor C on L.nroLicencia = C.nroLicencia
inner join Persona P on C.dni = P.dni
/*Filtrar por Dni*/
inner join 
		(
		select Dni, idSiniestro, 'Acompañante' as Participacion
		from siniestroacompañante
        
		union all  
		select dni, idSiniestro, 'Testigo' as Participacion
		from siniestroTestigo
		union all
		select dni, idSiniestro, 'Peaton' as Participacion
		from siniestroPeaton
		union all
		select dni, idSiniestro,  'Conductor' as Participacion
		from siniestroVehiculoConductor
		)as Participacion
	
    on Participacion.dni = P.dni
inner join Siniestro S on S.idSiniestro = Participacion.idSiniestro
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
$$

DELIMITER ;


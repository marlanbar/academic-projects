/*
Consulta por modalidad de accidentes viales: Obtener, dado una modalidad de 
accidente (atropello, vuelco, incendio, etc), un listado de licencias de 
conducir y la cantidad de veces que cada una de estas licencias incurrio en 
la modaldidad consultada.
*/

USE `tp1`;
DROP procedure IF EXISTS `DetalleDeAccidentesPorModalidad`;

DELIMITER $$
USE `tp1`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `DetalleDeAccidentesPorModalidad`(modalidad varchar(200))
BEGIN

select Licencia.NroLicencia, count(Siniestro.idSiniestro)
from TipoColision
inner join Siniestro on Siniestro.idTipoColision = TipoColision.idTipoColision 
inner join siniestrovehiculoconductor SVC on SVC.idSiniestro = Siniestro.idSiniestro 
inner join Conductor on  Conductor.DNI = SVC.DNI 
inner join Licencia on Conductor.nroLicencia = Licencia.nroLicencia
where TipoColision.Descripcion = modalidad
group by Licencia.NroLicencia;

END$$

DELIMITER ;

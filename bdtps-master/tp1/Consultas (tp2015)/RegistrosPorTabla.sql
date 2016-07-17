select tabla, registros from(
	select count(*) registros	,'acompañante' as tabla from acompañante
 union select count(*) registros ,'antecedente' as tabla from antecedente
 union select count(*) registros ,'autopista' as tabla from autopista
 union select count(*) registros ,'calle' as tabla from calle
 union select count(*) registros ,'categoria' as tabla from categoria
 union select count(*) registros ,'companiaaseguradora' as tabla from companiaaseguradora
 union select count(*) registros ,'condiciongeneral' as tabla from condiciongeneral
 union select count(*) registros ,'conductor' as tabla from conductor
 union select count(*) registros ,'conductorhabilitado' as tabla from conductorhabilitado
 union select count(*) registros ,'denuncia' as tabla from denuncia
 union select count(*) registros ,'estadoiluminacion' as tabla from estadoiluminacion
 union select count(*) registros ,'fuerealizadopor' as tabla from fuerealizadopor
 union select count(*) registros ,'funcionario' as tabla from funcionario
 union select count(*) registros ,'informe' as tabla from informe
 union select count(*) registros ,'infraccion' as tabla from infraccion
 union select count(*) registros ,'licencia' as tabla from licencia
 union select count(*) registros ,'lugar' as tabla from lugar
 union select count(*) registros ,'organismo' as tabla from organismo
 union select count(*) registros ,'peaton' as tabla from peaton
 union select count(*) registros ,'persona' as tabla from persona
 union select count(*) registros ,'poliza' as tabla from poliza
 union select count(*) registros ,'ruta' as tabla from ruta
 union select count(*) registros ,'siniestro' as tabla from siniestro
 union select count(*) registros ,'siniestroacompañante' as tabla from siniestroacompañante
 union select count(*) registros ,'siniestropeaton' as tabla from siniestropeaton
 union select count(*) registros ,'siniestrotestigo' as tabla from siniestrotestigo
 union select count(*) registros ,'siniestrovehiculoconductor' as tabla from siniestrovehiculoconductor
 union select count(*) registros ,'testigo' as tabla from testigo
 union select count(*) registros ,'tipoaccidente' as tabla from tipoaccidente
 union select count(*) registros ,'tipocausaprobable' as tabla from tipocausaprobable
 union select count(*) registros ,'tipocobertura' as tabla from tipocobertura
 union select count(*) registros ,'tipocolision' as tabla from tipocolision
 union select count(*) registros ,'tipocondicionclimatica' as tabla from tipocondicionclimatica
 union select count(*) registros ,'tipoestadovia' as tabla from tipoestadovia
 union select count(*) registros ,'tipoinforme' as tabla from tipoinforme
 union select count(*) registros ,'tipoinfraccion' as tabla from tipoinfraccion
 union select count(*) registros ,'tipolicencia' as tabla from tipolicencia
 union select count(*) registros ,'tipopavimento' as tabla from tipopavimento
 union select count(*) registros ,'tipovehiculo' as tabla from tipovehiculo
 union select count(*) registros ,'vehiculo' as tabla from vehiculo
 union select count(*) registros ,'viapublica' as tabla from viapublica
 ) as Cantidades
 where registros =0
 order by registros
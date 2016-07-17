DELIMITER //

CREATE TRIGGER TR_ParticipanteConductor
BEFORE INSERT
   ON siniestrovehiculoconductor FOR EACH ROW
   
BEGIN

   -- Insert record into audit table
   INSERT INTO participante
   ( dni,
     idSiniestro,
     TipoParticipacion)
   VALUES
   ( NEW.DNI,
     new.idSiniestro,
     'Conductor' );

END; //

DELIMITER ;
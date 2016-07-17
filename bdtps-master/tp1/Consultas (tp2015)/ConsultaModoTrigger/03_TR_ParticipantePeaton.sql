DELIMITER //

CREATE TRIGGER TR_ParticipantePeaton
BEFORE INSERT
   ON siniestroPeaton FOR EACH ROW
   
BEGIN

   -- Insert record into audit table
   INSERT INTO participante
   ( dni,
     idSiniestro,
     TipoParticipacion)
   VALUES
   ( NEW.DNI,
     new.idSiniestro,
     'Peaton' );

END; //

DELIMITER ;
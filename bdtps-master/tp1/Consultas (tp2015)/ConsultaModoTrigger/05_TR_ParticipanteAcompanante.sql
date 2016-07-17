DELIMITER //

CREATE TRIGGER TR_ParticipanteAcompanante
BEFORE INSERT
   ON siniestroacompañante FOR EACH ROW
   
BEGIN

   INSERT INTO participante
   ( dni,
     idSiniestro,
     TipoParticipacion)
   VALUES
   ( NEW.DNI,
     new.idSiniestro,
     'Acompañante' );

END; //

DELIMITER ;
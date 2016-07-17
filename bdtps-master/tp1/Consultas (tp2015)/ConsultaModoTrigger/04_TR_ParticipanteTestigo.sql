DELIMITER //

CREATE TRIGGER TR_ParticipanteTestigo
BEFORE INSERT
   ON siniestroTestigo FOR EACH ROW
   
BEGIN

   INSERT INTO participante
   ( dni,
     idSiniestro,
     TipoParticipacion)
   VALUES
   ( NEW.DNI,
     new.idSiniestro,
     'Tesigo' );

END; //

DELIMITER ;
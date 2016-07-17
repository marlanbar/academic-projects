CREATE TABLE `tp1`.`participante` (
  `DNI` INT NOT NULL COMMENT '',
  `idSiniestro` INT NOT NULL COMMENT '',
  `TipoParticipacion` VARCHAR(45) NOT NULL COMMENT '',
  PRIMARY KEY (`DNI`, `idSiniestro`)  COMMENT '');

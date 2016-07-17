CREATE VIEW Participantes AS
    SELECT 
        Dni, idSiniestro, 'Acompañante' AS Participacion
    FROM
        siniestroacompañante 
    UNION ALL SELECT 
        dni, idSiniestro, 'Testigo' AS Participacion
    FROM
        siniestroTestigo 
    UNION ALL SELECT 
        dni, idSiniestro, 'Peaton' AS Participacion
    FROM
        siniestroPeaton 
    UNION ALL SELECT 
        dni, idSiniestro, 'Conductor' AS Participacion
    FROM
        siniestroVehiculoConductor
import sqlite3
import time
import datetime


con = sqlite3.connect('TP1.db')
c = con.cursor()

numero_subasta = int(raw_input("Numero de subasta: "))
query_hay_subasta = 'SELECT * FROM PUBLICACION p WHERE p.idPublicacion = ' + str(numero_subasta) + " AND p.esSubasta = 1"
if(len(c.execute(query_hay_subasta).fetchall()) == 0):
    print("ERROR : NO EXISTE ESA SUBASTA")
else:
    usuario = str(raw_input("Nombre de Usuario: "))
    query_hay_usuario = "SELECT * FROM PERSONA p WHERE p.idUsuario = '" + usuario + "'"
    if(len(c.execute(query_hay_usuario).fetchall()) == 0):
        print("ERROR : NO EXISTE ESE USUARIO")
    else:
        valor_a_escribir = float(raw_input("Monto a escribir: "))
        query_elegir_valor_actual = 'SELECT r.monto, r.idUsuario FROM OFERTA r WHERE r.idPublicacion = ' + str(numero_subasta) + " ORDER BY r.monto DESC"
        entrar = False
        if(len(c.execute(query_elegir_valor_actual).fetchall()) == 0):
            usuario_actual = ""
            entrar = (valor_a_escribir > 0)
        else:
            valor_actual = c.execute(query_elegir_valor_actual).fetchone()[0]
            usuario_actual = c.execute(query_elegir_valor_actual).fetchone()[1]
            entrar = (valor_a_escribir >= valor_actual) & (valor_a_escribir < (valor_actual * 2))
        if(entrar):
            if(usuario_actual == usuario):
                print("ERROR : ESTA OFERTANDO EL MISMO USUARIO")
            else:
                timestampstr = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                query_insertar_valor_a_escribir = "INSERT INTO OFERTA (idUsuario, idPublicacion, timestamp, monto) VALUES ( '" + usuario + "', " + str(numero_subasta) + ", '" + timestampstr + "' , " + str(valor_a_escribir) + ")"
                c.execute(query_insertar_valor_a_escribir)
                con.commit()
        else:
            print("ERROR : VALOR DE INSERCION INVALIDO")

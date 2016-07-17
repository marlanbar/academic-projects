import random
import string

rounds = 25
round_size = 20000

for i in range (0, rounds):
    for j in range (0, round_size):
        id_publicacion = '{0:06}'.format(random.randint(0, 999999))
        tipo = ''.join(random.choice(['Producto', 'Servicio', 'Mixto']))
        print "db.publicaciones.insert({\"idPublicacion\":\"" + id_publicacion + "\", \"tipo\":\"" + tipo + "\"})"
    print "sh.status()"
    print "db.publicaciones.getShardDistribution()"

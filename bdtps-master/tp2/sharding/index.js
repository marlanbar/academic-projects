sh.enableSharding("test_sharding")
db.people.ensureIndex({"id_publicacion": 1})
sh.shardCollection("test_sharding.people", {"id_publicacion": 1} )
use test_sharding
sh.enableSharding("test_sharding")
db.people.ensureIndex({"_id": "hashed"})
sh.shardCollection("test_sharding.people", {"_id": "hashed"} )

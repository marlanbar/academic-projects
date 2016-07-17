rm -rf data
rm -f run_routing_service_log
#1) crear los shards
mkdir -p ./data/localhost10000
mongod --rest --shardsvr --port 10000 --dbpath data/localhost10000 --logpath data/localhost10000/log &
mkdir -p ./data/localhost10001
mongod --rest --shardsvr --port 10001 --dbpath data/localhost10001 --logpath data/localhost10001/log &
mkdir -p ./data/localhost10002
mongod --rest --shardsvr --port 10002 --dbpath data/localhost10002 --logpath data/localhost10002/log &
mkdir -p ./data/localhost10003
mongod --rest --shardsvr --port 10003 --dbpath data/localhost10003 --logpath data/localhost10003/log &
mkdir -p ./data/localhost10004
mongod --rest --shardsvr --port 10004 --dbpath data/localhost10004 --logpath data/localhost10004/log &

#2) Crear config server
mkdir -p ./data/localhost10005
mongod --rest --port 10005 --dbpath data/localhost10005 --logpath data/localhost10005/log &

#3) Crear routing service
mongos --port 10006 --configdb localhost:10005 > run_routing_service_log &

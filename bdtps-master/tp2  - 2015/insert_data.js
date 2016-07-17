var insertData = function(dbName, colName, num) {

  var col = db.getSiblingDB(dbName).getCollection(colName);

  for (i = 0; i < num; i++) {
    x = Math.floor(Math.random() * 1000000);
    doc = {
      nombre: 'Martin Juarez',
      password: 'asdasd' ,
      codigo_postal: x,
      genero: 'masculino',
      edad: 29,
      fecha_creacion: '30/02/2015'
    }
    col.insert(doc);
  }

  print(col.count());
  print(col.getShardDistribution());
  print("#########################################################################");
}

var insertDataTotal = function(dbName, colName, step, total) {

  var col = db.getSiblingDB(dbName).getCollection(colName);

  while(col.count() < total){
    for (i = 0; i < step; i++) {
      x = Math.floor(Math.random() * 1000000);
      doc = {
        nombre: 'Martin Juarez',
        password: 'asdasd' ,
        codigo_postal: x,
        genero: 'masculino',
        edad: 29,
        fecha_creacion: '30/02/2015'
      }
      col.insert(doc);
    }

    print(col.count());
    print(col.getShardDistribution());
    print("#########################################################################");
  }
}

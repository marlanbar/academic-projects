--  Para correr los tests deben cargar en hugs el módulo Tests
--  y evaluar la expresión "main".
-- Algunas funciones que pueden utilizar para chequear resultados:
-- http://hackage.haskell.org/package/hspec-expectations-0.6.1/docs/Test-Hspec-Expectations.html#t:Expectation

import Test.Hspec
import MapReduce


main :: IO ()
main = hspec $ do
  describe "Utilizando Diccionarios" $ do
    it "puede determinarse si un elemento es una clave o no" $ do
      belongs 3 [(3, "A"), (0, "R"), (7, "G")]    `shouldBe` True
      belongs "k" []                              `shouldBe` False
      [("H", [1]), ("E", [2]), ("Y", [0])] ? "R"  `shouldBe` False
      [("V", [1]), ("O", [2]), ("S", [0])] ? "V"  `shouldBe` True

    it "puede obtenerse el significado de una clave asumiendo que esta definida" $ do
      get 3 [(3, "A"), (0, "R"), (7, "G")]        `shouldBe` "A"
      [("A", 1), ("B", 2), ("C", 3)] ! "B"        `shouldBe` 2

    it "puede definir un nuevo valor para una clave dada, utilizando la funcion que reciba como parametro" $ do
      insertWith (++) 1 [99] [(1 , [1]) , (2 , [2])]  `shouldMatchList` [(1 ,[1 ,99]) ,(2 ,[2])]
      insertWith (++) 3 [99] [(1 , [1]) , (2 , [2])]  `shouldMatchList` [(1 ,[1]) ,(2 ,[2]) ,(3 ,[99])]
      
    it "puede agrupar los datos por clave, generando un diccionario que asocia a cada clave con la lista de todos sus valores" $ do
      groupByKey [("calle","Jean Jaures"), ("ciudad","Brujas"), ("ciudad","Kyoto"), ("calle","7")] 
      `shouldSatisfy` (\res -> iguales (significado res "calle") ["Jean Jaures", "7"] &&
                               iguales (significado res "ciudad") ["Kyoto", "Brujas"])

    it "puede unir dos diccionarios, utilizando la funcion que reciba como parametro en caso de conflicto entre claves" $ do
      unionWith (+) [] [("rutas", 3)] `shouldMatchList` [("rutas", 3)]
      unionWith (+) [("rutas", 3)] [] `shouldMatchList` [("rutas", 3)]
      unionWith (+) [("rutas", 3)] [("rutas", 4) , ("ciclos", 1)] `shouldMatchList` [("rutas", 7) ,("ciclos", 1)]
      unionWith (-) [("rutas", 4)] [("rutas", 3) , ("ciclos", 1)] `shouldMatchList` [("rutas", -1) ,("ciclos", 1)]

  describe "Utilizando Map Reduce" $ do
    it "dada una lista de elementos, divide la carga de manera balanceada entre una cantidad determinada de m maquinas" $ do
      distributionProcess 5 [1,2,3] `shouldMatchList` [[1],[2],[3],[],[]]
      distributionProcess 5 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] `shouldSatisfy` (\res -> and [ length x >= 2 | x <- res ])

    it "mapperProcess debe aplicar el mapper a cada uno de los elementos de tipo a y luego agrupar los resultados por clave." $ do
      mapperProcess (\(x, y) -> [(y, 1)]) [(1, "B"), (2, "D"), (3, "C"), (4, "D"), (1, "A"), (3, "D")] 
      `shouldMatchList` [("B", [1]), ("D", [1, 1, 1]), ("A", [1]),("C", [1])]

    it "combinerProcess se encarga de recibir la informacion resultante de cada maquina, y combina estos resultados de manera que queden agrupados por clave, y ordenados de manera creciente segun la clave" $ do
      combinerProcess [[("B", [1]), ("D", [1]), ("D", [1])], [("D", [1]), ("A", [1]),("C", [1])]] 
      `shouldMatchList` [("A", [1]), ("B", [1]), ("C", [1]), ("D", [1, 1, 1])]  

    it "reducerProcess se encarga de aplicar el reducer sobre cada par de elementos, y luego aplanar el resultado para unificar las soluciones" $ do
      reducerProcess (\(k, b) -> [(k, sum b)]) [("A", [1]), ("B", [1]), ("C", [1]), ("D", [1, 1, 1])] 
      `shouldBe` [("A", 1), ("B", 1), ("C", 1), ("D", 3)]
   
    it "mapReduce combina el combinerProcess y el reducerProcess" $ do
      mapReduce (\(x, y) -> [(y, 1)]) (\(k, b) -> [(k, sum b)]) [(1, "B"), (2, "D"), (3, "C"), (4, "D"), (1, "A"), (3, "D")] 
      `shouldMatchList` [("A", 1), ("B", 1), ("C", 1), ("D", 3)]
    
    it "visitas por monumento funciona en algún orden" $ do
      visitasPorMonumento [ "m1" ,"m2" ,"m3" ,"m2","m1", "m3", "m3"] `shouldMatchList` [("m3",3), ("m1",2), ("m2",2)] 
    
    it "monumentosTop devuelve los más visitados en algún orden" $ do 
      monumentosTop [ "m1", "m0", "m0", "m0", "m2", "m2", "m3"] 
      `shouldSatisfy` (\res -> res == ["m0", "m2", "m3", "m1"] || res == ["m0", "m2", "m1", "m3"])

    it "monumentosPorPais determina cuantos monumentos existen por cada pais. Se puede asumir que siempre estara definida la clave country" $ do
      monumentosPorPais items `shouldMatchList` [("Argentina", 2), ("Irak", 1)] 


       
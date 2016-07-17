module MapReduce where

import Data.Ord
import Data.List
import Data.Function
import Data.List (sort)
import Data.Tuple
iguales a b = sort a == sort b
significado dicc clave = foldr (\x acc -> (if clave == fst x then snd x else acc)) [] dicc
-- ---------------------------------Sección 1---------Diccionario ---------------------------
type Dict k v = [(k,v)]

-- Ejercicio 1

-- foldr recorre los elementos de la lista comenzando en False, y devolviendo True si lo encuentra
belongs :: Eq k => k -> Dict k v -> Bool
belongs k = foldr (\x b -> fst x == k || b) False

(?) :: Eq k => Dict k v -> k -> Bool
(?) = flip belongs
--Main> [("calle",[3]),("city",[2,1])] ? "city" 
--True

-- Ejercicio 2

-- realiza un filtrado de las tuplas obteniendo la tupla cuyo primer elemento sea igual a la clave, 
-- y devolviendo el segundo elemento de dicha tupla
get :: Eq k => k -> Dict k v -> v
get key dict = snd (head (filter (\t -> (fst t) == key) dict))

(!) :: Eq k => Dict k v -> k -> v
(!) = flip get
--Main> [("calle",[3]),("city",[2,1])] ! "city" 
--[2,1]

-- Ejercicio 3

-- si ya existe la clave dada realiza un map de la lista, donde solo cambia el significado cuya clave es la dada
-- si no existe se concatena un nuevo par con la clave y el significado dados  
insertWith :: Eq k => (v -> v -> v) -> k -> v -> Dict k v -> Dict k v
insertWith f key value dict = if belongs key dict 
                              then map (\par -> (if key == (fst par) then (fst par, (f (snd par) value)) else par)) dict 
                              else dict ++ [(key,value)] 
--Main> insertWith (++) 2 ['p'] (insertWith (++) 1 ['a','b'] (insertWith (++) 1 ['l'] []))
--[(1,"lab"),(2,"p")]

-- Ejercicio 4

-- crea una nueva lista recorriendo los elementos de la original con foldr, utilizando insertWith y la 
-- concatenacion para agrupar los valores por clave
groupByKey :: Eq k => [(k,v)] -> Dict k [v]
groupByKey = foldr (\par rec -> (insertWith (++) (fst par) [(snd par)] rec)) []

-- Ejercicio 5

-- recorre los elementos de las dos listas concatenadas en una lista nueva, utilizando insertWith y la 
-- funcion dada para agrupar los valores por clave
unionWith :: Eq k => (v -> v -> v) -> Dict k v -> Dict k v -> Dict k v
unionWith f dict1 dict2 = foldr (\par rec -> insertWith f (fst par) (snd par) rec) [] (dict1 ++ dict2)
--Main> unionWith (++) [("calle",[3]),("city",[2,1])] [("calle", [4]), ("altura", [1,3,2])]
--[("calle",[3,4]),("city",[2,1]),("altura",[1,3,2])]


-- ------------------------------Sección 2--------------MapReduce---------------------------

type Mapper a k v = a -> [(k,v)]
type Reducer k v b = (k, [v]) -> [b]

-- Ejercicio 6

-- comenzando con n sublistas vacias, por cada elemento a distribuir se lo coloca en la primera
-- sublista y luego se tira dicha sublista al final de todo
distributionProcess :: Int -> [a] -> [[a]]
distributionProcess n = foldr (\x rec -> (tail rec) ++ [(x:(head rec))] ) (replicate n [])

-- Ejercicio 7

-- se le aplica la funcion dada como parametro a cada elemento y luego se agrupa el resultado
-- de todas las aplicaciones con groupByKey
mapperProcess :: Eq k => Mapper a k v -> [a] -> [(k,[v])]
mapperProcess m as = groupByKey (foldr (\x rec -> (m x) ++ rec) [] as)

-- Ejercicio 8

-- se recorre el resultado de cada pc y se agrupa por clave, concatenando los significados
combinerProcess :: (Eq k, Ord k) => [[(k, [v])]] -> [(k,[v])]
combinerProcess result = sortBy (compare `on` fst) (foldr (\x rec -> (unionWith (++) x rec)) [] result)
--combinerProcess = foldr (\x rec -> sortBy (compare `on` fst) (unionWith (++) x rec)) []   

-- Ejercicio 9

-- se aplica la funcion de reduccion a cada tupla y se lo concatena a la lista
reducerProcess :: Reducer k v b -> [(k, [v])] -> [b]
reducerProcess r = foldr (\x rec -> (r x)++rec) []

-- Ejercicio 10

-- se distribuyen los datos entre 100 maquinas utilizando distributionProcess,
-- se le aplica la funcion de mapeo a los datos de cada maquina utilizando mapperProcess 
-- y la funcion mapeadora dada
-- se combinan los resultados de cada maquina por clave utilizando combinerProcess
-- se realiza la reduccion de cada par utilizando reducerProcess y la funcion reductora dada
mapReduce :: (Eq k, Ord k) => Mapper a k v -> Reducer k v b -> [a] -> [b]
mapReduce mapper reducer lsa = reducerProcess reducer (combinerProcess (map (mapperProcess mapper) (distributionProcess 100 lsa)))

-- Ejercicio 11

-- la funcion mapeadora convierte los datos en tuplas agrupados por nombre de monumento y un 1 por cada 
-- aparicion de dicho monumento
-- la funcion reductora agarra lo anterior y por cada tupla reemplaza la cantidad de 1s por su longitud
visitasPorMonumento :: [String] -> Dict String Int
visitasPorMonumento lst = mapReduce (\x -> [(x,1)]) (\x -> [(fst x, length(snd x))]) lst

-- Ejercicio 12

-- dada la lista de visitasPorMonumento se transforma la cantidad de cada uno a negativa y se los ordena
-- de menos a mayor, luego se deshace de la tupla y se queda con el nombre de cada monumento
--monumentosTop lst = [fst p | p <- (sortBy (compare `on` (\x-> -1*(snd x)) ) (visitasPorMonumento lst) ) ]
monumentosTop :: [String] -> [String]
monumentosTop lst = mapReduce (\(f, s) -> [( (-1*s), f)]) (\x -> snd x) (visitasPorMonumento lst)

-- Ejercicio 13 

-- la funcion mapeadora chequea si la esctructura es un monumento, en cuyo caso agarra el nombre del
-- pais y agrega un 1, caso contrario no hace nada
-- la funcion reductora agarra lo anterior y por cada tupla reemplaza la cantidad de 1s por su longitud
monumentosPorPais :: [(Structure, Dict String String)] -> [(String, Int)]
monumentosPorPais = mapReduce
                      (\x -> if (fst x) /= Monument then [] else [( (snd x) ! "country" , 1)]) 
                      (\x -> [(fst x, length(snd x))])


-- ------------------------ Ejemplo de datos del ejercicio 13 ----------------------
data Structure = Street | City | Monument deriving (Show, Eq)

items :: [(Structure, Dict String String)]
items = [
    (Monument, [
      ("name","Obelisco"),
      ("latlong","-36.6033,-57.3817"),
      ("country", "Argentina")]),
    (Street, [
      ("name","Int. Güiraldes"),
      ("latlong","-34.5454,-58.4386"),
      ("country", "Argentina")]),
    (Monument, [
      ("name", "San Martín"),
      ("country", "Argentina"),
      ("latlong", "-34.6033,-58.3817")]),
    (City, [
      ("name", "Paris"),
      ("country", "Francia"),
      ("latlong", "-24.6033,-18.3817")]),
    (Monument, [
      ("name", "Bagdad Bridge"),
      ("country", "Irak"),
      ("new_field", "new"),
      ("latlong", "-11.6033,-12.3817")])
    ]


------------------------------------------------
------------------------------------------------
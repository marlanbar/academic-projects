module Main where

import HUnit
import MapReduce
import Data.List (sort)	

--Ejercicio 1 (belongs)
dict1 :: Dict Int Int
dict1 = [(1,0),(2,1),(4,2),(8,3)]

dict2 :: Dict String [Int]
dict2 = [("Argentina",[78,86]),("Espana",[10]),("Uruguay",[30,50])]

testBelongs1 = TestCase (assertEqual "Test Belongs 1:" (belongs 2 dict1) (True))
testBelongs2 = TestCase (assertEqual "Test Belongs 2:" (belongs "Argentina" dict2) (True))
testBelongs3 = TestCase (assertEqual "Test Belongs 3:" (belongs "Brasil" dict2) (False))
testBelongs4 = TestCase (assertEqual "Test Belongs 4:" (dict2 ? "Uruguay") (True))
testBelongs5 = TestCase (assertEqual "Test Belongs 5:" (dict1 ? 10) (False))


--Ejercicio 2 (get)
testGet1 = TestCase (assertEqual "Test Get 1:" (get 1 dict1) (0))
testGet2 = TestCase (assertEqual "Test Get 2:" (get "Argentina" dict2) ([78,86]))
testGet3 = TestCase (assertEqual "Test Get 3:" (dict2 ! "Uruguay") ([30,50]))

--Ejercicio 3 (insertWith)
dict3 :: Dict String [Int]
dict3 = [("Argentina",[78,86,18]),("Espana",[10]),("Uruguay",[30,50])]

dict4 :: Dict String [Int]
dict4 = [("Argentina",[78,86]),("Espana",[10]),("Uruguay",[30,50]),("Colombia",[22])]

testInsertWith1 = TestCase (assertEqual "Test Insert With 1:" (insertWith (++) "Argentina" [18] dict2) (dict3))
testInsertWith2 = TestCase (assertEqual "Test Insert With 2:" (insertWith (++) "Colombia" [22] dict2) (dict4))

--Ejercicio 4 (groupByKey)
--Como el comportamiento esperado no esta determinado uso get que ya esta testeado
list1 :: [(String,Int)]
list1 = [("Uruguay",50),("Uruguay",30),("Argentina",86),("Espana",10),("Argentina",78)]

testGroupByKey1 = TestCase (assertEqual "Test Group By Key 1:" (get "Argentina" (groupByKey list1)) ([78,86]))

--Ejercicio 5 (unionWith)
--Aplica lo mismo que para el ejercicio 4
dict5 :: Dict Int Int
dict5 = [(4,1),(8,4)]

dict6 :: Dict String [Int]
dict6 = [("Argentina",[18]),("Francia",[98])]

testUnionWith1 = TestCase (assertEqual "Test Union With 1:" (get 4 (unionWith (+) dict1 dict5)) (3))
testUnionWith2 = TestCase (assertEqual "Test Union With 2:" (get "Francia" (unionWith (++) dict2 dict6)) ([98]))
testUnionWith3 = TestCase (assertEqual "Test Union With 3:" (length (get "Argentina" (unionWith (++) dict2 dict6))) (3))

--Ejercicio 6 (distributionProcess)
list2 :: [Int]
list2 = [1,2,3,4,5,2,3,4,5,6,3,4,5,6,7]

testDistributionProcess1 = TestCase (assertEqual "Test Distribution Process 1" (length (distributionProcess 4 list2)) (4))
testDistributionProcess2 = TestCase (assertEqual "Test Distribution Process 2" (maximum (foldr (\x y -> (length x):y) [] (distributionProcess 4 list2))) (4))
testDistributionProcess3 = TestCase (assertEqual "Test Distribution Process 3" (minimum (foldr (\x y -> (length x):y) [] (distributionProcess 4 list2))) (3))
testDistributionProcess4 = TestCase (assertEqual "Test Distribution Process 4" (sort (concat (distributionProcess 4 list2))) (sort list2))

--Ejercicio 7 (mapperProcess)


tests = TestList [	
					TestLabel "Test Belongs 1" testBelongs1,
					TestLabel "Test Belongs 2" testBelongs2,
					TestLabel "Test Belongs 3" testBelongs3,
					TestLabel "Test Belongs 4" testBelongs4,
					TestLabel "Test Belongs 5" testBelongs5,
					
					TestLabel "Test Get 1" testGet1,
					TestLabel "Test Get 2" testGet2,
					TestLabel "Test Get 3" testGet3,
					
					TestLabel "Test Insert With 1" testInsertWith1,
					TestLabel "Test Insert With 2" testInsertWith2,
					
					TestLabel "Test Group By Key 1" testGroupByKey1,
					
					TestLabel "Test Union With 1" testUnionWith1,
					TestLabel "Test Union With 2" testUnionWith2,
					TestLabel "Test Union With 3" testUnionWith3,
					
					TestLabel "Test Distribution Process 1" testDistributionProcess1,
					TestLabel "Test Distribution Process 2" testDistributionProcess2,
					TestLabel "Test Distribution Process 3" testDistributionProcess3,
					TestLabel "Test Distribution Process 4" testDistributionProcess4]
main = do runTestTT tests

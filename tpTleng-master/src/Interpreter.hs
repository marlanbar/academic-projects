module Main(main) where

import Language( evalProg )
import Grammar ( parseProg )

main :: IO ()
main = do
    s <- getContents
    case parseProg s of
      Left  e -> putStrLn ("error: " ++ e)
      Right p -> putStr $ foldr pairAndList [] (evalProg p)
        where pairAndList (a,b) str = show a++" "++show b++"\n"++str

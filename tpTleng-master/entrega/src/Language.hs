module Language where

import Data.Maybe
import Data.List

-- tipos para parser
type Arg = String
type Var = String
type Name = String

data Program = Program [Func] Exp Exp Var Exp Exp Exp
             deriving Show

data Func = Func Name [Arg] [Statement]
          deriving Show

data Statement = StmtReturn Exp
               | StmtAssign Var Exp
               | StmtIf BoolExp [Statement] [Statement]
               | StmtWhile BoolExp [Statement]
               deriving Show

data Exp = Plus Exp Exp
         | Minus Exp Exp
         | Times Exp Exp
         | Div Exp Exp
         | Pow Exp Exp
         | Negate Exp
         | Brack Exp
         | Num Double
         | Var String
         | Call Name [Exp]
         | Pi
         deriving Show

data BoolExp = And BoolExp BoolExp
             | Or  BoolExp BoolExp
             | Not BoolExp
             | Eq  Exp Exp
             | Gtr Exp Exp
             | Lwr Exp Exp
             | Geq Exp Exp
             | Leq Exp Exp
             deriving Show

-- tipos para interprete

-- vamos evaluando, mientras no encontremos un return,
-- alterando el environment de funcion (se devuelve un environment).
-- encontrado un return, devolvermos el double

type PartialEval = Either EnvFunc Double


-- nombres de funciones
data EnvProg = EnvProg [Func]

-- nombres de variables y variables asignadas
data EnvFunc = EnvFunc [Arg] [(Var,Double)]

funcName :: Func -> String
funcName (Func name _ _) = name

emptyEnvProg :: EnvProg
emptyEnvProg = EnvProg []


envProgLookup :: EnvProg -> Name -> Maybe Func
envProgLookup (EnvProg fs) name =
    find (\f -> funcName f == name) fs


emptyEnvFunc :: EnvFunc
emptyEnvFunc = EnvFunc [] []


envFuncLookup :: EnvFunc -> Var -> Maybe Double
envFuncLookup (EnvFunc _ sfs) var = lookup var sfs


envFuncBind :: EnvFunc -> Var -> Double -> EnvFunc
envFuncBind (EnvFunc ss sfs) var val =
    let asignar (varT,valT) lista = if varT==var
                                    then (var,val) : lista
                                    else (varT,valT) : lista
    in EnvFunc ss $ if isNothing (envFuncLookup (EnvFunc ss sfs) var)
                    --no esta
                    then sfs++[(var,val)]
                    else foldr asignar [] sfs


evalProg :: Program -> [(Double,Double)]
evalProg (Program funcs xCoord yCoord var rangeMin step rangeMax) =
    let -- el environment del programa (es decir, las funciones declaradas)
        envP = EnvProg funcs
        -- evaluamos los rangos en el contexto vacio
        simpleEval expr = evalExp expr emptyEnvFunc emptyEnvProg
        -- los puntos sobre los cuales se debe evaluar
        toEvaluate = takeWhile (<= simpleEval rangeMax) $ iterate (+simpleEval step) (simpleEval rangeMin)
        -- definimos la variable que corre por el rango en el environment
        env = envFuncBind emptyEnvFunc var
        -- toma un valor y evalua y lo appendea a la listprogEnv a
        eval val expr = evalExp expr (env val) envP
        -- evalua las dos coordenedas y lo appende a la lista
        evalCoords val lista = (eval val xCoord, eval val yCoord) : lista
        -- no queremos que haya funciones con el mismo nombre
        functionNames = map funcName funcs
    in case functionNames \\ nub functionNames
       of []       -> foldr evalCoords [] toEvaluate
          repeated -> error $ "\nRuntime error: funcion " ++ head repeated ++ " declarada mas de una vez"


evalExp :: Exp -> EnvFunc -> EnvProg -> Double
evalExp expr envF envP =
    let recursive expression = evalExp expression envF envP
    in case expr
       of (Brack e)     -> recursive e
          (Num v)       -> v
          (Pi)          -> pi
          (Plus e1 e2)  -> recursive e1 + recursive e2
          (Minus e1 e2) -> recursive e1 - recursive e2
          (Times e1 e2) -> recursive e1 * recursive e2
          (Div e1 e2)   -> recursive e1 / recursive e2
          (Pow e1 e2)   -> recursive e1 ** recursive e2
          (Negate e)    -> -recursive e
          (Var s)       -> fromMaybe (error $ "\nRuntime error: variable " ++ s ++ " no declarada")
                                     (envFuncLookup envF s)
          (Call s args) -> let -- evalua argumento y appendea
                               eval exprs list = recursive exprs : list
                               -- evaluamos argumentos para llamar a la funcion
                               instArgs = foldr eval [] args
                               func = fromMaybe (error $ "\nRuntime error: funcion " ++ s ++ " no declarada")
                                                (envProgLookup envP s)
                           in evalFunc func envP instArgs


evalFunc :: Func -> EnvProg -> [Double] -> Double
evalFunc (Func name args stmts) envP instArgs =
    let varsYvals = zip args instArgs 
        bindVar (var,val) envRec = envFuncBind envRec var val
        -- inicializamos el envFunc con los parametros de entrada
        envF = foldr bindVar emptyEnvFunc varsYvals
        -- calculamos el resultado de la funcion
        result = evalStatementList stmts envF envP
    -- evaluamos el return
    in if length args == length instArgs
       then case result
            of Left _    -> error $ "\nRuntime error: no se llego a un return en " ++ name
               Right res -> res
       else error $ "\nRuntime error: cantidad incorrecta de parametros en " ++ name


evalStatement :: Statement -> EnvFunc -> EnvProg -> PartialEval
evalStatement stmt envF envP =
                 -- si llegamos a un return, devolvemos el valor
    case stmt
    of (StmtReturn expr)           -> Right $ evalExp expr envF envP
       -- si es asignacion, la realizamos
       (StmtAssign var expr)       -> Left $ envFuncBind envF var (evalExp expr envF envP)
       -- si es un while, si la guarda da true
       (StmtWhile bexp stmts)      -> if evalBoolExp bexp envF envP
                                      -- si la evaluacion del bloque no da un resultado, evaluamos el while recursivamente
                                      then case blockEvaluation
                                           of Left envFNew -> evalStatement (StmtWhile bexp stmts) envFNew envP
                                              -- si no, devolvemos el resturn del bloque
                                              Right res    -> Right res
                                      -- si la guarda es false, devolvemos el environment que nos pasaron y seguimos
                                      else Left envF
                                          where blockEvaluation = evalStatementList stmts envF envP
       -- si es un if evaluamos el primer o segundo bloque segun la guarda
       (StmtIf bexp stmtsT stmtsF) -> evalStatementList theOne envF envP
           where theOne = if evalBoolExp bexp envF envP
                          then stmtsT
                          else stmtsF


-- recorremos los statements modificando el environment o retornamos el resultado el encontrar return
evalStatementList :: [Statement] -> EnvFunc -> EnvProg -> PartialEval
evalStatementList stmts envF envP =
    let statementEval resRec stmt = case resRec
                                    of Left envFRec -> evalStatement stmt envFRec envP 
                                       Right res    -> Right res
    in foldl statementEval (Left envF) stmts


evalBoolExp :: BoolExp -> EnvFunc -> EnvProg -> Bool
evalBoolExp bexp envF envP =
    let recursive bexpression = evalBoolExp bexpression envF envP
        expCase expression = evalExp expression envF envP
    in case bexp
       of (And bexp1 bexp2)  -> recursive bexp1 && recursive bexp2
          (Or bexp1 bexp2)   -> recursive bexp1 || recursive bexp2
          (Not bexp1)        -> not $ recursive bexp1
          (Eq exp1 exp2)     -> expCase exp1 == expCase exp2
          (Gtr exp1 exp2)    -> expCase exp1 > expCase exp2
          (Lwr exp1 exp2)    -> expCase exp1 < expCase exp2
          (Geq exp1 exp2)    -> expCase exp1 >= expCase exp2
          (Leq exp1 exp2)    -> expCase exp1 <= expCase exp2

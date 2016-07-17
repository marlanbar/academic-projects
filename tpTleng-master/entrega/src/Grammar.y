{
module Grammar( parseProg, readProg ) where

import Language
import Tokens
}

%name parse
%tokentype { Token }
%monad { Alex }
%lexer { lexwrap } { TokenEOF }
%error { happyError }

%token
    num { TokenNum $$ }
    var { TokenSym $$ }
    '=' { TokenAssign }
    '+' { TokenPlus }
    '-' { TokenMinus }
    '*' { TokenTimes }
    '/' { TokenDiv }
    '^' { TokenPow }
    '&&'{ TokenAnd }
    '||'{ TokenOr }
    '!' { TokenNot }
    '=='{ TokenEq }
    '<' { TokenLss }
    '>' { TokenGtr }
    '<='{ TokenLeq }
    '>='{ TokenGeq }
    '(' { TokenLParen }
    ')' { TokenRParen }
    '{' { TokenScopel }
    '}' { TokenScoper }
    ',' { TokenComma }
    '.' { TokenDot }
    if  { TokenIf }
    then{ TokenThen }
    else{ TokenElse }
    while { TokenWhile }
    pi  { TokenPi }
    function { TokenFunction }
    plot { TokenPlot }
    for { TokenRange }
    return { TokenReturn }


%right then else
-- el or se evalua antes que el and y el not antes todavia
%left '||'
%left '&&'
%left '!'
-- los siguientes operadores no asocian
%nonassoc '>' '<' '<=' '>=' '==' '='

-- las operaciones aritmeticas se evaluan antes que las operaciones logicas
-- el por y div se evalua antes que el + y -
%left '+' '-'
%left NEG
%left '*' '/'
--la potencia tiene mayor precedencia de los operadores binarios
%left '^'


%%

Program : Funcs plot
            '(' var '(' CallArgs ')'  ',' var '(' CallArgs ')'  ')'
            for var '=' Exp '.' '.' Exp '.' '.' Exp
                { Program $1 (Call $4 $6) (Call $9 $11) $15 $17 $20 $23 }

Funcs : Func                 { $1:[] }
      | Func Funcs           { $1:$2 }

Func : function var '(' Args ')' StatementsBlock { Func $2 $4 $6 }

StatementsBlock : Statement  { $1:[] }
                | '{' Statements '}' { $2 }

-- 0, 1 o mas statements
Statements : Statement       { $1:[] }
           | Statement Statements { $1:$2 }

Statement : var '=' Exp      { StmtAssign $1 $3 }
          | if BoolExp then StatementsBlock else StatementsBlock { StmtIf $2 $4 $6 }
          --el if puede o no tener else
          | if BoolExp then StatementsBlock { StmtIf $2 $4 [] }
          | while BoolExp StatementsBlock { StmtWhile $2 $3 }
          | return Exp       { StmtReturn $2 }

-- 0, 1 o mas argumentos
Args :                       { [] }
     | var                   { $1:[] }
     | var ',' Args          { $1:$3 }

BoolExp : BoolExp '&&' BoolExp { And $1 $3 }
        | BoolExp '||' BoolExp { Or $1 $3 }
        | '!' BoolExp        { Not $2 }
        | Exp '==' Exp       { Eq $1 $3 }
        | Exp '>' Exp        { Gtr $1 $3 }
        | Exp '<' Exp        { Lwr $1 $3 }
        | Exp '>=' Exp       { Geq $1 $3 }
        | Exp '<=' Exp       { Leq $1 $3 }

Exp : Exp '+' Exp            { Plus $1 $3 }
    | Exp '-' Exp            { Minus $1 $3 }
    | Exp '*' Exp            { Times $1 $3 }
    | Exp '/' Exp            { Div $1 $3 }
    | Exp '^' Exp            { Pow $1 $3 }
    | '(' Exp ')'            { $2 }
    | '-' Exp %prec NEG      { Negate $2 }
    | num                    { Num $1 }
    | var                    { Var $1 }
    | var '(' CallArgs ')'   { Call $1 $3 }
    | pi                     { Pi }

CallArgs :                   { [] }
         | Exp               { $1:[] }
         | Exp ',' CallArgs  { $1:$3 }

{

lexwrap :: (Token -> Alex a) -> Alex a
lexwrap cont = do
    t <- alexMonadScan'
    cont t


alexMonadScan' = do
    inp <- alexGetInput
    sc <- alexGetStartCode
    case alexScan inp sc of
        AlexEOF -> alexEOF
--      AlexError (pos, _, _, _) -> alexError (show pos)
        AlexError (pos, _, _, _) -> do
            (l,c) <- getPosn
            curStr <- getStr
            alexError (errorString l c "Error sintactico" curStr)
        AlexSkip  inp' len -> do
            alexSetInput inp'
            alexMonadScan'
        AlexToken inp' len action -> do
            alexSetInput inp'
            action (ignorePendingBytes inp) len

getPosn :: Alex (Int,Int)
getPosn = do
    (AlexPn _ c l,_,_,_) <- alexGetInput
    return (l,c)

getStr :: Alex String
getStr = do
    (_,_,_,currentString) <- alexGetInput
    return currentString

happyError :: Token -> Alex a
happyError t = do
    (l,c) <- getPosn
    curStr <- getStr
    fail (errorString l c "Error de parseo" curStr)

errorString :: Int -> Int -> String -> String -> String
errorString c l strg curStr =
    "\n" ++ show l ++ ":" ++ show c ++ ": " ++ strg ++ ". Justo antes de:\n\n" ++ (take 30 curStr) ++ "\n"

-- se le tira directo el string
parseProg :: String -> Either String Program
parseProg s = runAlex s parse

---- por si se quiere leer un programa de archivo
readProg :: FilePath -> IO (Either String Program)
readProg fp = do
    cs <- readFile fp
    return (parseProg cs)

}

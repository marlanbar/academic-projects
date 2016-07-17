{
module Tokens
  ( alexEOF
  , alexSetInput
  , alexGetInput
  , alexError
  , alexScan
  , ignorePendingBytes
  , alexGetStartCode
  , runAlex
  , Alex(..)
  , Token(..)
  , AlexReturn(..)
  , AlexPosn(..)
  ) where

import Prelude hiding (lex)
}

%wrapper "monad"

$digit = 0-9
$alpha = [a-zA-Z]

tokens :-


-- cualquier espacio en blanco no significa nada
  $white+                          ;

-- comentarios a la C
-- inicio comentario
<0>  "/*"                          { begin comment }
-- cualquier cosa que no sea asterisco
<comment> [^ \* ]*                 ;
-- asteriscos que no esten seguidos de una /
<comment> \*+ [^ \* \/ ]*          ;
-- fin del comentario
<comment> "*/"                     { begin 0 }

<0>  \+                            { lex' TokenPlus }
<0>  \-                            { lex' TokenMinus }
<0>  \*                            { lex' TokenTimes }
<0>  \/                            { lex' TokenDiv }
<0>  \^                            { lex' TokenPow }
<0>  \(                            { lex' TokenLParen }
<0>  \)                            { lex' TokenRParen }
<0>  "&&"                          { lex' TokenAnd }
<0>  "||"                          { lex' TokenOr }
<0>  \!                            { lex' TokenNot }
<0>  \=                            { lex' TokenAssign }
<0>  "=="                          { lex' TokenEq }
<0>  "<"                           { lex' TokenLss }
<0>  ">"                           { lex' TokenGtr }
<0>  "<="                          { lex' TokenLeq }
<0>  ">="                          { lex' TokenGeq }
<0>  "{"                           { lex' TokenScopel }
<0>  "}"                           { lex' TokenScoper }
<0>  \,                            { lex' TokenComma }
<0>  \.                            { lex' TokenDot }
<0>  pi                            { lex' TokenPi }
<0>  function                      { lex' TokenFunction }
<0>  return                        { lex' TokenReturn }
<0>  while                         { lex' TokenWhile }
<0>  if                            { lex' TokenIf }
<0>  then                          { lex' TokenThen }
<0>  else                          { lex' TokenElse }
<0>  plot                          { lex' TokenPlot }
<0>  for                           { lex' TokenRange }
<0>  $digit+ (\. $digit+)?         { lex (TokenNum . read) }
<0>  $alpha [$alpha $digit \_ \']* { lex TokenSym }

{

data Token = TokenNum Double
           | TokenSym String
           | TokenEq
           | TokenPlus
           | TokenMinus
           | TokenTimes
           | TokenDiv
           | TokenPow
           | TokenLParen
           | TokenRParen
           | TokenAnd
           | TokenOr
           | TokenNot
           | TokenAssign
           | TokenLss
           | TokenGtr
           | TokenLeq
           | TokenGeq
           | TokenScopel
           | TokenScoper
           | TokenFunction
           | TokenReturn
           | TokenWhile
           | TokenIf
           | TokenThen
           | TokenElse
           | TokenPi
           | TokenPlot
           | TokenRange
           | TokenComma
           | TokenDot
           | TokenEOF
           deriving (Eq,Show)

alexEOF = return TokenEOF

-- tokens dependientes del input
lex :: (String -> a) -> AlexAction a
lex f = \(_,_,_,s) i -> return (f (take i s))

-- tokens independientes del input
lex' :: a -> AlexAction a
lex' = lex . const
}

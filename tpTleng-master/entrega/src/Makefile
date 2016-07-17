all: Interpreter 

Tokens.hs : Tokens.x
	alex Tokens.x

Grammar.hs : Grammar.y
	happy Grammar.y
    
Interpreter : Tokens.hs Grammar.hs Interpreter.hs
	ghc --make Interpreter
    
clean:
	rm -f Interpreter Grammar.hs Tokens.hs *.o *.hi

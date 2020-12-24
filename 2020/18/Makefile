# Makefile for PLT lab 2 in Java

# Variables for file lists
###########################################################################

LABSRC    = Interpreter.java

PARSERSRC = $(wildcard Grammar/Absyn/*.java Grammar/*.java)
PARSEROBJ = $(PARSERSRC:.java=.class)
LABOBJ    = $(LABSRC:.java=.class)

# Variables for the programming environment
###########################################################################

# Name of generated .cup file for bnfc ≥ 2.8.1
CUPFILE = Grammar/_cup.cup

JAVAC       = javac
JAVAC_FLAGS = -sourcepath .
JAVA        = java

# No need to edit these:
javac       = ${JAVAC} ${JAVAC_FLAGS}
java        = ${JAVA}  ${JAVA_FLAGS}

# Default rule
###########################################################################

# List of goals not corresponding to file names.
.PHONY : default all clean

default : Interpreter.class

all : default

# Rules for compiling classes
###########################################################################

Interpreter.class : Interpreter.java Grammar/Test.class
	$(javac) $<


# Rules for creating the parser
###########################################################################

# Create parser source via bnfc (dependency Grammar.cf needs to be first).
Grammar/Yylex $(CUPFILE) Grammar/Test.java : Grammar.cf
	bnfc --java $<

# Create parser and move it to the correct location.
Grammar/parser.java Grammar/sym.java : $(CUPFILE)
	$(java) java_cup.Main -package Grammar $<
	mv parser.java sym.java Grammar/

# Create lexer.
Grammar/Yylex.java : Grammar/Yylex
	$(java) JLex.Main $<

# Compile lexer.
Grammar/Yylex.class : Grammar/Yylex.java Grammar/sym.class
	$(javac) $<

# Create parser test.
Grammar/Test.class : Grammar/Test.java Grammar/parser.class Grammar/sym.class Grammar/Yylex.class
	$(javac) $<


# Default rules
###########################################################################

%.class : %.java
	$(javac) $<


# Rules for cleaning generated files
###########################################################################

clean :
	-rm -f Grammar/Absyn/*.class Grammar/*.class
	-rm -f Grammar.dvi Grammar.aux Grammar.log Grammar.ps
	-rm -f $(LABOBJ)
	-rm -f *.class


vclean : clean
	-rm -f $(PARSERSRC)
	-rm -f Grammar/Absyn/*.bak Grammar/*.bak
	-rmdir Grammar/Absyn/
	-rm -f Grammar.tex
	-rm -f Grammar/Yylex $(CUPFILE)
	-rmdir -p Grammar/

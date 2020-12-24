import Grammar.*;
import Grammar.Absyn.*;
import java.io.FileReader;
import java.util.List;

public class Interpreter {
    /*
      I happened to be taking this course:
        http://www.cse.chalmers.se/edu/course/DAT151/
      while doing this puzzle, so it's mostly copy-pasting parts from a lab we had.

      Since BNFC can't handle whitespaces as separators
        see https://github.com/BNFC/bnfc/issues/55
      I appended semicolons to each line in the input.
    */
    public static void main(String[] args) throws Exception {
        Yylex lexer = new Yylex(new FileReader(args[0]));
        parser p = new parser(lexer);
        Grammar.Absyn.Hwork parse_tree = p.pHwork();
        System.out.println(new Interpreter().interpret(parse_tree));
    }

    private long sum = 0;

    public long interpret(Hwork hwork) {
        List<Exp> expressions = ((HDef) hwork).listexp_;
        for (Exp e : expressions) {
            sum += e.accept(new ExpVisitor(), null);
        }
        return sum;
    }

    private static class ExpVisitor implements Exp.Visitor<Long, Void> {
        public Long visit(EInt e, Void arg) {
            return (long) e.integer_;
        }

        public Long visit(EAdd e, Void arg) {
            return e.exp_1.accept(new ExpVisitor(), null) + e.exp_2.accept(new ExpVisitor(), null);
        }

        public Long visit(EMul e, Void arg) {
            return e.exp_1.accept(new ExpVisitor(), null) * e.exp_2.accept(new ExpVisitor(), null);
        }
    }
}

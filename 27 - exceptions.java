import java.util.Scanner;


public class Exception {

    public static void main(String [] args) {

        int n1, n2;
        int division;
        Scanner input = new Scanner(System.in);
        
        System.out.println("CALCULADORA DE DIVISÃO DE NÚMEROS INTEIROS");
        System.out.println();
        System.out.println("Digite o valor do dividendo: ");
        n1 = input.nextInt();
        System.out.println("Digite o valor do divisor: ");
        n2 = input.nextInt();
        input.close();

        try {
            division = n1 / n2;
            System.out.println(n1 + "/" + n2 + " = " + division);
        } catch (ArithmeticException e) {
            System.out.println("A divisão pelo divisor 0 não é válida!");
        }

        System.out.println("Fim do programa");
    }
}

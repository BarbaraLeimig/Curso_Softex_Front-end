import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Ser_obj {
    
    public static void main(String [] args) {
        serializar();
        desserializar();
    }

    public static void serializar() {
        Objetos_papelaria o1 = new Objetos_papelaria("caderno", "azul");
        FileOutputStream a = null;
        ObjectOutputStream b = null;
        
        try {
        // o arquivo será criado na mesma pasta do programa, com o nome "exemplo"
        a = new FileOutputStream("exemplo.txt"); 
        b = new ObjectOutputStream(a);
        // serialização do objeto o1
        b.writeObject(o1); 

        // situações que podem ocorrer ao tentar serializar o objeto
        } catch (FileNotFoundException e) { 
            System.out.println("O arquivo não foi encontrado");
        } catch (IOException e) {
            System.out.println("Erro ao tentar criar o arquivo");

        // fechar o arquivo, caso tenha sido serializado com sucesso
        } finally {
            if (b != null) {
                try {
                    b.close();
                } catch (IOException e) {
                    System.out.println("Erro ao tentar fechar o arquivo");
                }
            }
        }
    }

    public static void desserializar() {
        Objetos_papelaria o1 = null;
        FileInputStream a = null;
        ObjectInputStream b = null;

        try {
            a = new FileInputStream("exemplo.txt");
            b = new ObjectInputStream(a);

            // convertendo o objeto que está sendo desserializado para classe Objetos_papelaria
            o1 = (Objetos_papelaria)b.readObject();

            // exibição dos dados do objeto
            System.out.printf("Nome: %s\nIdade: %d\nSalário: R$%.2f\nNúmero de vendas: %d",
            o1.getObjeto(), o1.getCor());

        // situações que podem ocorrer ao tentar desserializar o objeto
        } catch (ClassNotFoundException e) { 
            System.out.println("A classe não foi encontrada");
        } catch (IOException e) {
            System.out.println("Erro ao tentar criar o arquivo");

        // se o objeto b(desserealizador) for diferente de nulo, o arquivo será fechado
        } finally {
            if (b != null) {
                try {
                    b.close();
                } catch (IOException e) {
                    System.out.println("Erro ao tentar fechar o arquivo");
                }
            }
        }
    }
}
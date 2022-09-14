import java.io.Serializable;

public class Objetos_papelaria implements Serializable{

    public String objeto;
    public String cor;
    
    public Objetos_papelaria(String objeto, String cor) {
        this.objeto = objeto;
        this.cor = cor;
    }

    public String getObjeto() {
        return objeto;
    }

    public void setObjeto(String objeto) {
        this.objeto = objeto;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

}

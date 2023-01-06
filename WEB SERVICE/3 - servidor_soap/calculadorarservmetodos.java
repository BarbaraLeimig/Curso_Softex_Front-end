// Aqui serão implementados os métodos definidos anteriormente. 

package calc;

import java.util.Date;
import javax.jws.WebService;

@WebService(endpointInterface = "calc.CalculadoraServer")

/* A propriedade endpointInterface faz com que a classe atual, a SIB, ligue-se com a SEI 
especificada anteriormente (calc.CalculadoraServer).*/

public class CalculadoraServerImpl implements CalculadoraServer {

  public float soma(float num1, float num2) {
    return num1 + num2;
  }

  public float subtracao(float num1, float num2) {
    return num1 - num2;
  }

  public float multiplicacao(float num1, float num2) {
    return num1 * num2;
  }

  public float divisao(float num1, float num2) {
    return num1 / num2;
  }

}
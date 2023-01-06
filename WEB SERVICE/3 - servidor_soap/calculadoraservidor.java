/*
Aqui vamos criar uma Web Service simples dividindo pela parte da interface, SEI (Service Endpoint Interface),
e a implementação, que é chamada de SIB (Service Implementation Bean).
O objetivo deste serviço é retornar o calculo de uma das operações invocadas pelo cliente.
 */

 package calc;

 import javax.jws.WebService;
 import javax.jws.WebMethod;
 import javax.jws.soap.SOAPBinding;
 import javax.jws.soap.SOAPBinding.Style;
 
 @WebService // Aqui é uma anotação que avisa ao compilador Java que o arquivo atual corresponde à definição SEI de um serviço Web.
 
 @SOAPBinding(style = Style.RPC)
 public interface CalculadoraServer {
   @WebMethod float soma(float num1, float num2);
   @WebMethod float subtracao(float num1, float num2);
   @WebMethod float multiplicacao(float num1, float num2);
   @WebMethod float divisao(float num1, float num2);
 }
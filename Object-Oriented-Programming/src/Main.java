package src;

import java.util.Scanner;
import src.Vault.Vault;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard_listener = new Scanner(System.in);
        System.out.println("----- Sistema de Cofre de Moedas -----\n");

        Vault vault = new Vault();
        boolean running = true;
        while (running) {
            System.out.println("|=| O que deseja fazer com seu cofre? |=|");
            System.out.println("1 - Adicionar moeda");
            System.out.println("2 - Remover moeda");
            System.out.println("3 - Listar todas as moedas");
            System.out.println("4 - Calcular valor total do cofre em reais");
            System.out.println("5 - Fechar cofre");
            
            System.out.print("Opção: ");
            int option = keyboard_listener.nextInt();
            
            switch (option) {
                case 1:
                    System.out.println("\n");
                    System.out.println("|=| Qual moeda deseja adicionar? |=|");
                    System.out.println("1 - Real");
                    System.out.println("2 - Dolar");
                    System.out.println("3 - Euro");
                    System.out.println("4 - Retornar");

                    vault.addCoin(null);
                    break;
                
                case 2:
                    System.out.println("\n");
                    vault.removeCoin(null);
                    break;
                
                case 3:
                    System.out.println("\n");
                    vault.listCoins();
                    break;

                case 4:
                    System.out.println("\n");
                    vault.calculateVaultValue();
                    break;
                
                case 5:
                    System.out.println("\n");
                    System.out.println("Fechando cofre...");
                    System.out.println("Cofre fechado com sucesso!");
                    running = false;
                    break;
            
                default:
                    System.out.println("\n");
                    System.out.println("A opção " + option + " não existe, por favor escolha uma opção válida.");
                    System.out.println("\n");
                    break;
            }
        }
        
        keyboard_listener.close();
    }
}

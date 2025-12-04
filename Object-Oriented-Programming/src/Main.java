package src;

import java.util.Scanner;
import src.Vault.Vault;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard_listener = new Scanner(System.in);
        System.out.println("----- Sistema de Cofre de Moedas -----");

        Vault vault = new Vault();
        boolean running = true;
        while (running) {
            System.out.println("|=| O que deseja fazer com seu cofre? |=|");

            String[] options = new String[]{
                "Adicionar moeda", "Remover moeda", "Listar todas as moedas",
                "Calcular valor total do cofre em reais", "Fechar cofre"
            };
            for (int i = 0; i < options.length; i++) {
                System.out.println((i + 1) + " - " + options[i]);
            }
            
            int option;
            try {
                System.out.print("Opção: ");
                option = keyboard_listener.nextInt();
            } catch (Exception error) {
                System.out.println("Erro! Por favor escolha uma opção válida.");
                keyboard_listener.next();
                continue;
            }
            
            switch (option) {
                case 1:
                    System.out.println("\n");
                    System.out.println("|=| Qual moeda deseja adicionar? |=|");

                    options = new String[]{"Real", "Dolar", "Euro", "Retornar"};
                    for (int i = 0; i < options.length; i++) {
                        System.out.println((i + 1) + " - " + options[i]);
                    }

                    try {
                        System.out.print("Opção: ");
                        option = keyboard_listener.nextInt();
                    } catch (Exception error) {
                        System.out.println("Erro! Por favor escolha uma opção válida.");
                        keyboard_listener.next();
                        continue;
                    }

                    if (option < 1 || option > 4) {
                        System.out.println("A opção " + option + " não existe, por favor escolha uma opção válida.");
                        continue;
                    }
                    else if (option == 4) {
                        System.out.println("Retornando ao menu principal...");
                        break;
                    }
                    
                    double value;
                    try {
                        System.out.print("Valor em " + options[option - 1] + " a ser adicionado: ");
                        value = keyboard_listener.nextDouble();
                    } catch (Exception error) {
                        System.out.println("Erro! Por favor escolha uma opção válida.");
                        keyboard_listener.next();
                        continue;
                    }

                    vault.addCoin(value, option);
                    break;
                
                case 2:
                    vault.removeCoin(null);
                    break;
                
                case 3:
                    vault.listCoins();
                    break;

                case 4:
                    vault.calculateVaultValue();
                    break;
                
                case 5:
                    System.out.println("Fechando cofre...");
                    System.out.println("Cofre fechado com sucesso!");
                    running = false;
                    break;
            
                default:
                    System.out.println("A opção " + option + " não existe, por favor escolha uma opção válida.");
                    break;
            }
        }
        
        keyboard_listener.close();
    }
}

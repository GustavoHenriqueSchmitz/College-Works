package src;

import java.util.Scanner;
import src.Vault.Vault;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard_listener = new Scanner(System.in);
        Vault vault = new Vault();
        boolean running = true;

        System.out.println("\n");
        System.out.println("========================================");
        System.out.println("<=>    SISTEMA DE COFRE DE MOEDAS    <=>");
        System.out.println("========================================");

        while (running) {
            System.out.println("\n========== MENU PRINCIPAL ==========");
            String[] options = new String[]{
                "Adicionar moeda", "Remover moeda", "Listar moedas",
                "Calcular total (R$)", "Fechar cofre"
            };
            
            for (int i = 0; i < options.length; i++) {
                System.out.println((i + 1) + " - " + options[i]);
            }
            System.out.println("====================================");
            
            int option;
            try {
                System.out.print("Escolha uma opção: ");
                option = keyboard_listener.nextInt();
            } catch (Exception error) {
                System.out.println("\n>> Erro! Apenas valores númericos são aceitos.");
                keyboard_listener.next();
                continue;
            }
            
            switch (option) {
                case 1:
                    System.out.println("\n------- ADICIONAR MOEDA -------");
                    options = new String[]{"Real", "Dolar", "Euro", "Voltar"};
                    for (int i = 0; i < options.length; i++) {
                        System.out.println((i + 1) + " - " + options[i]);
                    }

                    int coinChoice;
                    try {
                        System.out.print("Escolha o tipo: ");
                        coinChoice = keyboard_listener.nextInt();
                    } catch (Exception error) {
                        System.out.println("\n>> Erro! Opção inválida.");
                        keyboard_listener.next();
                        continue;
                    }

                    if (coinChoice < 1 || coinChoice > 4) {
                        System.out.println("\n>> Opção inválida.");
                        continue;
                    }
                    else if (coinChoice == 4) {
                        System.out.println("Cancelando...");
                        break;
                    }
                    
                    double value;
                    try {
                        System.out.print("Valor em " + options[coinChoice - 1] + ": ");
                        value = keyboard_listener.nextDouble();
                    } catch (Exception error) {
                        System.out.println("\n>> Erro! Valor inválido (use vírgula para decimais).");
                        keyboard_listener.next();
                        continue;
                    }

                    vault.addCoin(value, coinChoice);
                    break;
                
                case 2:
                    System.out.println("\n------- REMOVER MOEDA -------");
                    
                    vault.listCoins();
                    System.out.println("0. Retornar");
                    try {
                        System.out.print("Digite o número da moeda que deseja remover: ");
                        option = keyboard_listener.nextInt();
                    } catch (Exception error) {
                        System.out.println("\n>> Erro! Apenas valores númericos são aceitos.");
                        keyboard_listener.next();
                        continue;
                    }

                    if (option == 0) {
                        continue;
                    }
                    
                    try {
                        vault.removeCoin(option - 1);
                    } catch (IndexOutOfBoundsException error) {
                        System.out.println("\n>> Erro: Índice inválido (Moeda não existe).");
                        continue;
                    }
                    break;
                
                case 3:
                    vault.listCoins();
                    break;

                case 4:
                    vault.calculateVaultValue();
                    break;
                
                case 5:
                    System.out.println("\n========================================");
                    System.out.println("<=>         ENCERRANDO SISTEMA        <=>");
                    System.out.println("========================================");
                    running = false;
                    break;
            
                default:
                    System.out.println("\n>> Opção desconhecida.");
                    break;
            }
        }
        
        keyboard_listener.close();
    }
}

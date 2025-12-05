package src;

import java.util.Scanner;
import src.Vault.Vault;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard_listener = new Scanner(System.in);
        Vault vault = new Vault(); // Instancia o cofre
        boolean running = true; // Controle do loop principal

        System.out.println("\n");
        System.out.println("========================================");
        System.out.println("<=>    SISTEMA DE COFRE DE MOEDAS    <=>");
        System.out.println("========================================");

        // Loop principal do menu
        while (running) {
            System.out.println("\n========== MENU PRINCIPAL ==========");
            String[] options = new String[]{
                "Adicionar moeda", "Remover moeda", "Listar moedas",
                "Calcular total (R$)", "Fechar cofre"
            };
            
            // Exibe as opções numeradas
            for (int i = 0; i < options.length; i++) {
                System.out.println((i + 1) + " - " + options[i]);
            }
            System.out.println("====================================");
            
            // Pergunta e válida a opção selecionada pelo usuário
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
                case 1: // --- ADICIONAR MOEDA ---
                    System.out.println("\n------- ADICIONAR MOEDA -------");
                    options = new String[]{"Real", "Dolar", "Euro", "Voltar"};
                    for (int i = 0; i < options.length; i++) {
                        System.out.println((i + 1) + " - " + options[i]);
                    } // Exibe as opções numeradas

                    // Pergunta e válida a opção selecionada pelo usuário
                    int coinChoice;
                    try {
                        System.out.print("Escolha o tipo: ");
                        coinChoice = keyboard_listener.nextInt();
                    } catch (Exception error) {
                        System.out.println("\n>> Erro! Opção inválida.");
                        keyboard_listener.next();
                        continue;
                    }

                    // Valida se a opção está entre 1 e 4, ou seja, se ela é válida
                    if (coinChoice < 1 || coinChoice > 4) {
                        System.out.println("\n>> Opção inválida.");
                        continue;
                    }
                    else if (coinChoice == 4) {
                        System.out.println("Cancelando...");
                        break;
                    }
                    
                    // Lê e válida o valor monetário a ser adicionado
                    double value;
                    try {
                        System.out.print("Valor em " + options[coinChoice - 1] + ": ");
                        value = keyboard_listener.nextDouble();
                    } catch (Exception error) {
                        System.out.println("\n>> Erro! Valor inválido (use vírgula para decimais).");
                        keyboard_listener.next();
                        continue;
                    }

                    // Chama o cofre para adicionar a moeda
                    vault.addCoin(value, coinChoice);
                    break;
                
                case 2: // --- REMOVER MOEDA ---
                    System.out.println("\n------- REMOVER MOEDA -------");
                    
                    // Lista primeiro para o usuário saber o índice, e pergunta e válida a opção selecionada
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

                    // Caso opção selecionada seja 0, cancela a operação de remoção
                    if (option == 0) {
                        continue;
                    }
                    
                    // Realiza a remoção do valor escolhido pelo usuário
                    try {
                        vault.removeCoin(option - 1);
                    } catch (IndexOutOfBoundsException error) {
                        System.out.println("\n>> Erro: Índice inválido (Moeda não existe).");
                        continue;
                    }
                    break;
                
                case 3: // --- LISTAR MOEDAS ---
                    vault.listCoins();
                    break;

                case 4: // --- CALCULAR TOTAL ---
                    vault.calculateVaultValue();
                    break;
                
                case 5: // --- SAIR ---
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

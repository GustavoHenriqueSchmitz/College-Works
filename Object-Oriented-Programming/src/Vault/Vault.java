package src.Vault;

import java.util.ArrayList;

// Classe Vault (Cofrinho) responsável por gerenciar a coleção de moedas
public class Vault {
    // Lista que armazena objetos do tipo genérico 'Coin'.
    private ArrayList<Coin> coinsList = new ArrayList<>();

    // Método para adicionar moedas.
    public void addCoin(double value, int coinType) {
        Coin coin = null;

        // Estrutura de decisão para criar a moeda correta
        switch (coinType) {
            case 1: coin = new Real(value); break;
            case 2: coin = new Dolar(value); break;
            case 3: coin = new Euro(value); break;
            default:
                System.out.println(">> Erro: Tipo de moeda inválido!");
                return;
        }

        // Se a moeda foi criada com sucesso, adiciona à lista
        if (coin != null) {
            this.coinsList.add(coin);
            System.out.println("--------------------------------");
            System.out.println("v  Moeda adicionada ao cofre!  v");
            System.out.println("--------------------------------");
        }
    }

    // Remove uma moeda baseada no índice da lista
    public void removeCoin(int coinIndex) {
        // Não precisamos de lógica extra pois o Main já valida o índice.
        this.coinsList.remove(coinIndex);

        System.out.println("--------------------------------");
        System.out.println("v   Moeda removida com sucesso! v");
        System.out.println("--------------------------------");
    }

    // Lista todas as moedas presentes no cofre
    public void listCoins() {
        System.out.println("\n---------- MOEDAS NO COFRE ----------");
        
        if (this.coinsList.isEmpty()) {
            System.out.println("           (Cofre Vazio)             ");
            System.out.println("-------------------------------------");
            return;
        }
        
        // Percorre a lista exibindo o índice (i + 1) e chamando o info() de cada moeda.
        for (int index = 0; index < this.coinsList.size(); index++) {
            System.out.print((index + 1) + ". ");
            this.coinsList.get(index).info();
        }
    }

    // Calcula o valor total convertido para Reais
    public void calculateVaultValue() {
        System.out.println("\n-------- VALOR TOTAL CONVERTIDO --------");
        if (this.coinsList.isEmpty()) {
            System.out.println("Total: R$ 0,00");
        } else {
            double total = 0;
            // Percorre todas as moedas somando seus valores convertidos
            for (Coin coin : this.coinsList) {
                total += coin.convert();
            }
            System.out.printf("Total acumulado: R$ %.2f%n", total); // Exibe o total formatado
        }
        System.out.println("----------------------------------------");
    }
}

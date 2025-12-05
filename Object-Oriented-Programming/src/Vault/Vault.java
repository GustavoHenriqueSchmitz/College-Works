package src.Vault;

import java.util.ArrayList;

public class Vault {
    private ArrayList<Coin> coinsList = new ArrayList<>();

    public void addCoin(double value, int coinType) {
        Coin coin = null;

        switch (coinType) {
            case 1: coin = new Real(value); break;
            case 2: coin = new Dolar(value); break;
            case 3: coin = new Euro(value); break;
            default:
                System.out.println(">> Erro: Tipo de moeda inválido!");
                return;
        }

        if (coin != null) {
            this.coinsList.add(coin);
            System.out.println("--------------------------------");
            System.out.println("v  Moeda adicionada ao cofre!  v");
            System.out.println("--------------------------------");
        }
    }

    public void removeCoin(int coinIndex) {
        this.coinsList.remove(coinIndex);

        System.out.println("--------------------------------");
        System.out.println("v   Moeda removida com sucesso! v");
        System.out.println("--------------------------------");
    }

    public void listCoins() {
        System.out.println("\n---------- MOEDAS NO COFRE ----------");
        
        if (this.coinsList.isEmpty()) {
            System.out.println("           (Cofre Vazio)             ");
            System.out.println("-------------------------------------");
            return;
        }

        for (int index = 0; index < this.coinsList.size(); index++) {
            System.out.print((index + 1) + ". ");
            this.coinsList.get(index).info();
        }
    }

    public void calculateVaultValue() {
        System.out.println("\n-------- VALOR TOTAL CONVERTIDO --------");
        if (this.coinsList.isEmpty()) {
            System.out.println("Total: R$ 0,00");
        } else {
            double total = 0;
            for (Coin coin : this.coinsList) {
                total += coin.convert();
            }
            System.out.printf("Total acumulado: R$ %.2f%n", total);
        }
        System.out.println("----------------------------------------");
    }
}

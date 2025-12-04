package src.Vault;

import java.util.ArrayList;

public class Vault {
    private ArrayList<Coin> coinsList = new ArrayList<>();

    public void addCoin(double value, int coinType) {
        Coin coin = null;

        switch (coinType) {
            case 1:
                coin = new Real(value);
                break;
            case 2:
                coin = new Dolar(value);
                break;
            case 3:
                coin = new Euro(value);
                break;
            default:
                System.out.println("Tipo de moeda inválido!");
                return;
        }

        if (coin != null) {
            this.coinsList.add(coin);
            System.out.println("Moeda adicionada ao cofre!");
        }
    }

    public void removeCoin(Coin coin) {
        this.coinsList.remove(coin);
    }

    public void listCoins() {
        if (this.coinsList.isEmpty()) {
            System.out.println("Cofre vazio.");
            return;
        }

        for (int i = 0; i < this.coinsList.size(); i++) {
            System.out.print(i + ". "); 
            this.coinsList.get(i).info();
        }
    }

    public void calculateVaultValue() {

    }
}

package src.Vault;

import java.util.ArrayList;

public class Vault {
    private ArrayList<Coin> coinsList = new ArrayList<>();

    public void addCoin(Coin coin) {
        this.coinsList.add(coin);
    }

    public void removeCoin(Coin coin) {
        this.coinsList.remove(coin);
    }

    public void listCoins() {

    }

    public void calculateVaultValue() {

    }
}

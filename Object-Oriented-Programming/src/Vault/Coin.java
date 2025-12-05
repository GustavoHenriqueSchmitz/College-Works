package src.Vault;

// Classe abstrata 'Coin' (Moeda) que serve de modelo para todas as moedas.
public abstract class Coin {
    public double value;

    public Coin(double value) {
        this.value = value;
    }

    public abstract void info();
    public abstract double convert();
}

// Subclasse Dolar herdando de Coin
class Dolar extends Coin {
    public Dolar(double value) { super(value); }

    @Override
    public void info() {
        System.out.printf("Dolar - US$ %.2f%n", value);
    }

    @Override
    public double convert() { return value * 5.2; }
}

// Subclasse Euro herdando de Coin
class Euro extends Coin {
    public Euro(double value) { super(value); }

    @Override
    public void info() {
        System.out.printf("Euro  - € %.2f%n", value);
    }

    @Override
    public double convert() { return value * 6.1; }
}

// Subclasse Real herdando de Coin
class Real extends Coin {
    public Real(double value) { super(value); }

    @Override
    public void info() {
        System.out.printf("Real  - R$ %.2f%n", value);
    }

    @Override
    public double convert() { return value * 1.0; }
}

package src.Vault;

public abstract class Coin {
    public double value;

    public Coin(double value) {
        this.value = value;
    }

    public abstract void info();
    public abstract double convert();
}

class Dolar extends Coin {
    public Dolar(double value) { super(value); }

    @Override
    public void info() {
        System.out.printf("Dolar - US$ %.2f%n", value);
    }

    @Override
    public double convert() { return value * 5.2; }
}

class Euro extends Coin {
    public Euro(double value) { super(value); }

    @Override
    public void info() {
        System.out.printf("Euro  - € %.2f%n", value);
    }

    @Override
    public double convert() { return value * 6.1; }
}

class Real extends Coin {
    public Real(double value) { super(value); }

    @Override
    public void info() {
        System.out.printf("Real  - R$ %.2f%n", value);
    }

    @Override
    public double convert() { return value * 1.0; }
}

package src.Vault;

public abstract class Coin {
    public double value;

    public abstract void info();
    public abstract double convert();
}

class Dolar extends Coin {
    @Override
    public void info() {}

    @Override
    public double convert() {
        return 0.0;
    }
    
}

class Euro extends Coin {
    @Override
    public void info() {}

    @Override
    public double convert() {
        return 0.0;
    }
    
}

class Real extends Coin {
    @Override
    public void info() {}

    @Override
    public double convert() {
        return 0.0;
    }
    
}

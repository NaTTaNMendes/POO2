package e7.model;

public class Carro {
    
    private String placa;
    private String cor;

    public Carro(String placa, String cor) {
        this.placa = placa;
        this.cor = cor;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }
    
    
}

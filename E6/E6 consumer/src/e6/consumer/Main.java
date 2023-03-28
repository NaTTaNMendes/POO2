package e6.consumer;

import e6.Programmer;
import e6.enums.Seniority;

public class Main {

    public static void main(String[] args) {
        Programmer prog1 = new Programmer("Nattan", "Mendes Tinonin", Seniority.JUNIOR.JUNIOR, 3000.0);
        System.out.println(prog1.introduce());
        System.out.println(prog1.complain());
    }
    
}

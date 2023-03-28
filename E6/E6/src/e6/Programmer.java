package e6;

import e6.enums.Seniority;

public class Programmer {
    
    private String name;
    private String surname;
    private Seniority seniority;
    private Double salary;

    public Programmer() {
    }

    public Programmer(String name, String surname, Seniority seniority, Double salary) {
        this.name = name;
        this.surname = surname;
        this.seniority = seniority;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public Seniority getSeniority() {
        return seniority;
    }

    public void setSeniority(Seniority seniority) {
        this.seniority = seniority;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }
    
    public String introduce() {
        return "My name is " + this.name + " " + this.surname + ", my seniority is " + seniority.toString() + " and my salary is " + salary;
    }
    
    public String complain() {
        if (this.seniority.equals(Seniority.JUNIOR)) {
            return "I hate Java";
        }
        if (this.seniority.equals(Seniority.INTERMEDIATE)) {
            return "I hate C++";
        }
        if (this.seniority.equals(Seniority.SENIOR)) {
            return "I hate C";
        }
        return "I hate my life";        
    } 
}

Programmer Seniority Program

This program demonstrates the use of an Enum in Java to represent the seniority of a programmer. The Seniority Enum has four possible values: JUNIOR, INTERMEDIATE, SENIOR, and LEAD.

The Programmer class has four fields: name, surname, seniority, and salary. It also has two methods: introduce() and complain(). The introduce() method returns a string that introduces the programmer, including their name and seniority. The complain() method returns a string that complains some programming language, based on their seniority.

Usage
To use this program, you will need to have Java installed on your machine. You can then compile and run the program using the following commands:


	Copy code
	$ javac Main.java
	$ java Main

The output should be as follows:

	My name is Nattan Mendes Tinonin, my seniority is JUNIOR and my salary is 3000.0
	I hate Java


Classes
Main
The Main class contains the main() method, which creates an instance of the Programmer class and calls its introduce() and complain() methods.

Seniority
The Seniority enum represents the seniority of a programmer, with four possible values: JUNIOR, INTERMEDIATE, SENIOR, and LEAD.

Programmer
The Programmer class represents a programmer, with fields for their name, seniority, and salary. It also has methods to introduce the programmer and complain about some programming language, based on their seniority.
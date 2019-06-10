//Benjamin Page
//6/4/2019
//Problem 2-- Extends Problem 1 by adding a main class that creates objects for each subclass, and calls the object's animalSound() method.


class Animal{
public void animalSound(){
System.out.println("The animal makes a sound");
}
}

class Pig extends Animal
{
public void animalSound()
{
System.out.println("The pig oink");
}
}

class Dog extends Animal
{
public void animalSound()
{
System.out.println("The dog barks");
}
}

class Cat extends Animal
{
public void animalSound()
{
System.out.println("The cat meows.");
}
}

public class mainClass
{
public static void main(String[] args)
{
Animal pigObj = new Pig();
Animal dogObj = new Dog();
Animal catObj = new Cat();
pigObj.animalSound();
dogObj.animalSound();
catObj.animalSound();

}
}
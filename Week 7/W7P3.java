//Benjamin Page
//5/21/2019
//Problem 3 -- Extend Problem 2 by creating multiple objects of sampleClass and change the attribute value in one object without affecting the attribute value in the other.

public class sampleClass {
  int x = 15;

  public static void main(String[] args) {
    sampleClass myObj1 = new sampleClass();
	myObj1.x = 20;
	sampleClass myObj2 = new sampleClass();
	System.out.println(myObj1.x);
    System.out.println(myObj2.x);
  }
}

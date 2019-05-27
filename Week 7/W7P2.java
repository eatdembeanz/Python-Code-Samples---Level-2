// Benjamin Page
// 5/21/2019
// Problem 2 -- Extends Probelm1 by setting the object x to a value within sampleClass and overrides that value within the main.

public class sampleClass {
  int x = 15;

  public static void main(String[] args) {
    sampleClass myObj = new sampleClass();
	System.out.println(myObj.x);
	myObj.x = 20;
	System.out.println(myObj.x);
  }
}

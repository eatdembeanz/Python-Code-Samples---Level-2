//Benjamin Page

//5/14/2019

//Module 6 Problem 5

//Problem 5 -- Extend problem 4 by adding a line that accesses and prints the attributes using dot syntax.

public class sampleClass
{
			int x = 5;
			int y = 50;

	public static void main(String []args)
	{
		sampleClass sampleObject = new sampleClass();
		System.out.println(sampleObject.x);
		System.out.println(sampleObject.y);
		
		sampleClass sampleObject2 = new sampleClass();
		System.out.println(sampleObject2.x);
		System.out.println(sampleObject.y);
	}
	
}
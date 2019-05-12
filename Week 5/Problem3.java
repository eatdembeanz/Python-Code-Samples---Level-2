/*Benjamin Page
5/7/2019
Problem 3-- Declares, assign values to, and prints examples of: byte,short,int,float,long,double,char,Boolean,and String.*/

class Problem3
{
	public static void main(String[] args)
	{
		byte a = 12;
		//Bytes are exclusively numbers, within a certain range.
		short b = 15;
		int c = 2000;
		long d = 1000000;
		//Longs are a datatype that allows for incredibly long strings of numbers.
		float e = 12.5f;
		//Floats MUST be ended with 'f'.
		double f = 12.5;
		char g = 'c';
		Boolean h = true;
		String i = "Hello";
		
		System.out.println(a + "/n" + b + "/n"+ c + "/n" + d + "/n" + e + "/n" + f + "/n" + g + "/n" + h +  "/n" + i);
	}
}
//Benjamin Page
//6/4/2019
//Problem 3: Extends the following code sample by adding a fourth bank, and its rate of interest.
class Bank{  
	float getRateOfInterest(){return 0;}  
}  
class SBI extends Bank{  
	float getRateOfInterest(){return 8.4f;}  
}  
class ICICI extends Bank{  
	float getRateOfInterest(){return 7.3f;}  
}  
class AXIS extends Bank{  
	float getRateOfInterest(){return 9.7f;}  
}
class NANO extends Bank{
	float getRateOfInterest(){return 10.0f;}
}

public class TestPolymorphism{  
	public static void main(String args[]){  
		Bank b;  
		b=new SBI();  
		System.out.println("SBI Rate of Interest: "+b.getRateOfInterest());  
		b=new ICICI();  
		System.out.println("ICICI Rate of Interest: "+b.getRateOfInterest());  
		b=new AXIS();  
		System.out.println("AXIS Rate of Interest: "+b.getRateOfInterest()); 
		b = new NANO();
		System.out.println("Nano Rate of Interest: "+b.getRateOfInterest());
	}  
}  

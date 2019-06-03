//Benjamin Page
//5/28/2019

//Problems 1 through 3
/*Take a code sample and set the object within the Person class as private.
Create a getter and setter for the class from Problem 1.
Create a main that will create a new object from the Person class, set the name to your name, and access and print the object.
*/

public class Person 
{
  private String name; // set to private = restricted access
public String getName()
	{
		return name; // Finds the variable 'name' set for the object.
	}
public void setName(String newName)
	{
		name = newName; //Overrides the object's current variable 'name' with whatever is given for 'newName'
	}
public static void main(String[] args)
	{
		Person myName = new Person();
		myName.getName();
		myName.setName("Benjamin Page");
		System.out.println(myName.name);
	}
	}

/* Benjamin Page
5/21/2019
Problem 4 -- Modify the Die class to keep a record of all the values the dice has rolled.
*/
import java.util.*;
/*
public class Die
{
   private int lastValue;

   public int roll()
   {
      lastValue = (int) (Math.random() * 6) + 1;
      return lastValue;
   }

   public static void main(String[] args)
   {
	 int intArray[] = new int[10];
      Die d = new Die();
      for (int i = 0; i < 10; i++)
      {
        intArray[i]=d.roll();
		System.out.println("Roll " + (i+1) + " is " + intArray[i]);
      }
	  System.out.println(Arrays.toString(intArray));
   }
 }


public class Die
{
   private int lastValue;
	private ArrayList<Integer> die_list = new ArrayList<Integer>(10);
   public int roll()
   {
      lastValue = (int) (Math.random() * 6) + 1;
	  die_list.add(lastValue);
      return lastValue;
   }

   public static void main(String[] args)
   {
      Die d = new Die();
      for (int i = 0; i < 10; i++)
      {
		System.out.println(d.roll());
		}
   }
 }

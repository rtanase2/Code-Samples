import java.util.HashMap;
import java.util.Scanner;

public class HungryPuppies {
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("\nWelcome to my Hungry Puppies Simulator!");
        System.out.println("Please enter a line of integers separated by spaces to denote treat size.");
        System.out.println("Ex: 1 1 2 2 2 4 7");
        System.out.println("You can type \"quit\" at any time to exit the program.\n");

        while(true){
            System.out.println("Please enter the treats Annie has:");
            String line = in.nextLine();
            if(line.equals("quit")){
                break;
            } else {
                findMaxHappiness(line);
            }
        }    
    }

    public static void findMaxHappiness(String s){
        HashMap<Integer, Integer> treatCount = new HashMap<Integer, Integer> ();
        String[] temp = s.split(" ");
        for(int i = 0; i < temp.length; i++){
            addToHashMap(treatCount, Integer.parseInt(temp[i]));
        }
        System.out.println(treatCount);
    }

    public static void addToHashMap(HashMap<Integer, Integer> hm, int x){
        if(hm.containsKey(x)){
            incVal(hm, x);
        } else {
            hm.put(x, 1);
        }
    }

    public static void incVal(HashMap<Integer, Integer> hm, int x){
        int temp = hm.get(x);
        hm.remove(x);
        hm.put(x, ++temp);
    }
    
    public static void createHLLHPattern(HashMap<Integer, Integer> treatCount) {
        for(int key : treatCount.keySet()) {
            System.out.println(key);
        }
    }
}
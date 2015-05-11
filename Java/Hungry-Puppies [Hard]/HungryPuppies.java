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
                String[] results = findBestOrder(line);
                System.out.println(results[0]);
                System.out.println(addSpaces(results[1].split("")) + "\n");
            }
        }    
    }

    private static String addSpaces(String[] a){
        String results = "";
        for (String s : a){
            results += s + " ";
        }
        return results;
    }

    public static String[] findBestOrder(String s){
        HashMap<Integer, Integer> treatCount = new HashMap<Integer, Integer> ();
        String[] temp = s.split(" ");
        for(int i = 0; i < temp.length; i++){
            addToHashMap(treatCount, Integer.parseInt(temp[i]));
        }
        String[] ret = new String[2];
        String result = createHLLHPattern(treatCount);
        while (true){
            if(treatCount.size() >= 2 && hasAtLeast2OfASize(treatCount)){
                result = addAnotherHLLH(treatCount, result);
            } 
            else if (treatCount.isEmpty()){
                //if there are no treats left, you are done!
                ret[1] = result;
                break;
            }
            else {
                //has any number of elems, but only one of each size
                ret[1] = sortRemainingTreats(treatCount, result);
                break;
            }
        }
        ret[0] = calcHappiness(ret[1]);
        return(ret);
    }

    public static String calcHappiness(String order){
        int happiness = 0;
        for (int i = 0; i < order.length(); i++){
            if (i == 0){
                if ((char)order.charAt(1) < (char)order.charAt(0)){
                    happiness += 1;
                }
                else if ((char)order.charAt(1) != (char)order.charAt(0)){
                    happiness -= 1;
                }
            }
            else if (i == order.length()-1){
                if ((char)order.charAt(i) < (char)order.charAt(i-1)){
                    happiness -= 1;
                }
                else if ((char)order.charAt(i) != (char)order.charAt(i-1)){
                    happiness += 1;
                }
            }
            else {
                Boolean gTLeft = (char)order.charAt(i) > (char)order.charAt(i-1);
                Boolean gTRight = (char)order.charAt(i) > (char)order.charAt(i+1);
                Boolean lTLeft = (char)order.charAt(i) < (char)order.charAt(i-1);
                Boolean lTRight = (char)order.charAt(i) < (char)order.charAt(i+1);
                if(gTRight && gTLeft){
                    happiness += 1;
                }
                else if(lTLeft && lTRight){
                    happiness -= 1;
                }
            }
        }
        return (Integer.toString(happiness));
    }

    public static String sortRemainingTreats(HashMap<Integer, Integer> hm, String curr){
        int[] used = new int[hm.size()];
        int index = 0;
        for (int k : hm.keySet()){
            int leftEdge = Integer.parseInt(Character.toString(curr.charAt(0)));
            int rightEdge = Integer.parseInt(Character.toString(curr.charAt(curr.length() - 1)));
            Boolean actionDone = false;
            if (k >= rightEdge){
                for(int j : hm.keySet()){
                    if(j < rightEdge && !in(used, j)){
                        //then it is less than k and forms "sandwich" (aka High-Low-High)
                        //ex: 324 is accepted
                        curr += Integer.toString(j) + Integer.toString(k);
                        used[index++] = j;
                        used[index++] = k;
                        actionDone = true;
                        break;
                    }
                }
                if (!actionDone){
                    curr += k;
                    used[index++] = k;
                }
                rightEdge = k;
            }
            else if (k >= leftEdge){
                for(int j : hm.keySet()){
                    if(j < leftEdge && !in(used, j)){
                        //then it is less than k and forms "sandwich" (aka High-Low-High)
                        //ex: 324 is accepted
                        curr = k + j + curr;
                        used[index++] = j;
                        used[index++] = k;
                        actionDone = true;
                        break;
                    }
                }
                if (!actionDone){
                    curr = k + curr; 
                    used[index++] = k; 
                }
                leftEdge = k;
            }
            actionDone = false;
        }
        return(curr);
    }

    public static Boolean in(int[] a, int x){
        for (int i : a){
            if(x==i){
                return true;
            }
        }
        return false;
    }

    public static Boolean hasAtLeast2OfASize(HashMap<Integer, Integer> hm){
        for (int key : hm.keySet()){
            if (hm.get(key) > 1){
                return true;
            }
        }
        return false;
    }

    public static String addAnotherHLLH(HashMap<Integer, Integer> hm, String curr){
        int leftEdge = Integer.parseInt(Character.toString(curr.charAt(0)));
        int rightEdge = Integer.parseInt(Character.toString(curr.charAt(curr.length() - 1)));
        int middleElem = 0; 
        int middleSize = 0;

        for (int key : hm.keySet()){
            if(hm.get(key) >= 2){
                if (key < leftEdge || key < rightEdge){
                    middleElem = key;
                    if(hm.get(key)%2 == 1){
                        middleSize = 3;
                    } else {
                        middleSize = 2;
                    }
                    break;
                }
            }
        }

        for (int key : hm.keySet()){
            if(key > middleElem){
                if(middleElem < rightEdge){
                    curr += repeat(middleElem, middleSize) + key;
                } else {
                    curr = key + repeat(middleElem, middleSize) + curr;
                }
                reduceCountInHashMap(hm, key, 1);
                reduceCountInHashMap(hm, middleElem, middleSize);
                break;
            }
        }
        return curr;
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
    
    public static String createHLLHPattern(HashMap<Integer, Integer> hm) {
        //Precondition, there are at least 2 numbers with 2 or more elements
        int highest = 0;
        int secondHighest = 0;
        int middleSize = 0;
        for(int key : hm.keySet()) {
            if(hm.get(key) >= 2){
                if (key > highest){
                    secondHighest = highest;
                    highest = key;
                } 
                else if (key > secondHighest){
                    secondHighest = key;
                }
            }
        }
        if (hm.get(secondHighest) % 2 == 1){
            middleSize = 3;
        } else {
            middleSize = 2;
        }
        reduceCountInHashMap(hm, highest, 2);
        reduceCountInHashMap(hm, secondHighest, middleSize);
        return (highest + repeat(secondHighest, middleSize) + highest);
    }

    public static void reduceCountInHashMap(HashMap<Integer, Integer> hm, int h, int size){
        int temp = hm.get(h);
        hm.remove(h);
        if(temp-size > 0){
            hm.put(h, temp-size);
        }
    }

    private static String repeat(int x, int times){
        String result = "";
        for (int i = 0; i < times; i++) {
            result += x;
        }
        return result;
    }
}
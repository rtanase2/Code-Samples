import java.util.HashMap;

public class HungryPuppies {
  
    public static void main(String[] args) {
        HashMap<Integer, Integer> treatCount = new HashMap<Integer, Integer> ();
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
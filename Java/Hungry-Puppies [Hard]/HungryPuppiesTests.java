import java.util.HashMap;

public class HungryPuppiesTests {

    public static void main(String[] args) {
        runTests();
    }
    
    private static void runTests() {

        System.out.println("\nRunning addToHashMap tests...");
        System.out.println("--------------------------------------");
        testAddToHashMap();   
        System.out.println("--------------------------------------\n");

        System.out.println("\nRunning incVal tests...");
        System.out.println("--------------------------------------");
        testIncVal();   
        System.out.println("--------------------------------------\n");

        System.out.println("\nRunning reduceCountInHashMap tests...");
        System.out.println("--------------------------------------");
        testReduceCountInHashMap();   
        System.out.println("--------------------------------------\n");

        System.out.println("\nRunning findCreateHLLHPattern tests...");
        System.out.println("--------------------------------------");
        testCreateHLLHPattern();   
        System.out.println("--------------------------------------\n");

        System.out.println("\nRunning addAnotherHLLH tests...");
        System.out.println("--------------------------------------");
        testAddAnotherHLLH();   
        System.out.println("--------------------------------------\n");

        System.out.println("\nRunning findBestOrder tests...");
        System.out.println("--------------------------------------");
        testFindBestOrder();   
        System.out.println("--------------------------------------\n");
        
    }

    private static void testAddAnotherHLLH(){
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer> ();
        String temp = "5335";
        int numTests = 2;
        int numSuccesses = 0;

        System.out.println("Attmpting to create another HLLH with 2 pairs in HashMap... ");
        hm.put(4, 2);
        hm.put(1, 2);
        temp = HungryPuppies.addAnotherHLLH(hm, temp);
        numSuccesses += printStatus(temp.equals("5335114") && hm.size() == 1);

        System.out.println("Attempting to create HLLH pattern one pair in HashMap... ");
        hm = new HashMap<Integer, Integer> ();
        hm.put(1, 2);
        hm.put(6, 1);
        temp = HungryPuppies.addAnotherHLLH(hm, temp);
        numSuccesses += printStatus(temp.equals("5335114116") && hm.size() == 0);

        printResult(numSuccesses, numTests);
    }

    private static void testCreateHLLHPattern(){
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer> ();
        String temp;
        int numTests = 4;
        int numSuccesses = 0;

        System.out.println("Attempting to create HLLH pattern with odd lower values... ");
        hm.put(3, 2);
        hm.put(2, 3);
        temp = HungryPuppies.createHLLHPattern(hm);
        numSuccesses += printStatus(temp.equals("32223"));

        System.out.println("Attempting to create HLLH pattern with odd higher values... ");
        hm = new HashMap<Integer, Integer> ();
        hm.put(3, 3);
        hm.put(2, 2);
        temp = HungryPuppies.createHLLHPattern(hm);
        numSuccesses += printStatus(temp.equals("3223"));
        
        System.out.println("Attempting to create HLLH pattern with both even values... ");
        hm = new HashMap<Integer, Integer> ();
        hm.put(3, 2);
        hm.put(2, 2);
        temp = HungryPuppies.createHLLHPattern(hm);
        numSuccesses += printStatus(temp.equals("3223"));

        System.out.println("Attempting to create HLLH pattern with both odd values... ");
        hm = new HashMap<Integer, Integer> ();
        hm.put(3, 3);
        hm.put(2, 3);
        temp = HungryPuppies.createHLLHPattern(hm);
        numSuccesses += printStatus(temp.equals("32223"));

        printResult(numSuccesses, numTests);
    }
    
    private static void testFindBestOrder(){
        String[] temp = new String[2];
        int numTests = 3;
        int numSuccesses = 0;

        System.out.println("Attempting to find maximum happiness of 1 1 1 1 1 2 2 3... ");
        temp = HungryPuppies.findBestOrder("1 1 1 1 1 2 2 3");
        numSuccesses += printStatus(temp[0] == "3" && temp[1] == "21112113");

        System.out.println("Attempting to find maximum happiness of 1 2 2 3 3 3 4... ");
        temp = HungryPuppies.findBestOrder("1 2 2 3 3 3 4");
        numSuccesses += printStatus(temp[0] == "2" && temp[1] == "3223134");

        System.out.println("Attempting to find maximum happiness of 1 1 2 3 3 3 3 4 5 5... ");
        temp = HungryPuppies.findBestOrder("1 1 2 3 3 3 3 4 5 5");
        numSuccesses += printStatus(temp[0] == "4" && temp[1] == "4335335112");

        printResult(numSuccesses, numTests);
    }

    private static void testIncVal(){
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer> ();
        int numTests = 1;
        int numSuccesses = 0;

        System.out.print("Attempting to increment an existing element... ");
        hm.put(1, 2);
        HungryPuppies.incVal(hm, 1);
        numSuccesses += printStatus(hm.get(1) == 3);

        printResult(numSuccesses, numTests);
    }

    private static void testReduceCountInHashMap(){
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer> ();
        int numTests = 2;
        int numSuccesses = 0;

        System.out.print("Attempting to decrease an element to zero count... ");
        hm.put(1, 2);
        HungryPuppies.reduceCountInHashMap(hm, 1, 2);
        numSuccesses += printStatus(hm.get(1) == null);

        System.out.print("Attempting to decrease an element to non-zero count... ");
        hm.put(1, 3);
        HungryPuppies.reduceCountInHashMap(hm, 1, 2);
        numSuccesses += printStatus(hm.get(1) == 1);

        printResult(numSuccesses, numTests);
    }

    private static void testAddToHashMap(){
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer> ();
        int numTests = 3;
        int numSuccesses = 0;

        System.out.print("Attempt to add unique element... ");
        HungryPuppies.addToHashMap(hm, 1);
        numSuccesses += printStatus(hm.get(1) == 1);

        System.out.print("Attempt to add duplicate element... ");
        HungryPuppies.addToHashMap(hm, 1);
        numSuccesses += printStatus(hm.get(1) == 2);

        System.out.print("Attempt to add another unique element... ");
        HungryPuppies.addToHashMap(hm, 2);
        numSuccesses += printStatus(hm.get(1) == 2 && hm.get(2) == 1);

        printResult(numSuccesses, numTests);
    }

    private static int printStatus(Boolean b){
        if (b){
            System.out.println("Success.");
            return(1);
        }
        else {
            System.out.println("Fail.");
            return(0);
        }
    }

    private static void printResult(int suc, int tot){
        System.out.println(suc + " out of " + tot + " succeeded.");
        System.out.println((tot-suc) + " out of " + tot + " failed.\n");
        if (suc == tot){
            System.out.println("OK.");
        } else {
            System.out.println("FAIL.");
        }
    }
}
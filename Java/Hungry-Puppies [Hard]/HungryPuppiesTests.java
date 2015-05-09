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
    }
    
    private static void testIncVal(){
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer> ();
        int numTests = 1;
        int numSuccesses = 0;

        System.out.print("Attempt to increment an existing element... ");
        hm.put(1, 2);
        HungryPuppies.incVal(hm, 1);
        numSuccesses += printStatus(hm.get(1) == 3);

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
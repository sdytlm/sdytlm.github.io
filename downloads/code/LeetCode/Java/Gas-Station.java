public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int start = 0;
        int balance = 0;
        int totalGas = 0;
        int totalCost = 0;
        for(int i=0;i<gas.length;i++){
            totalGal += gas[i];
            totalCost += cost[i];
            balance += gas[i]-cost[i];
            if(balance < 0){
                start = i+1;
                balance = 0;
            }
        }
        if(totalGas>=totalCost) return start;
        else return -1;    
    }
}

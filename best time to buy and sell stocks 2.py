class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        for(int i=1;i<prices.size();i++){

        int d1=prices[i];
        int d2=prices[i-1];
        int p=d1-d2;
        if (d2<d1)profit+=p;
        }
        return profit;
    }

        
    
};

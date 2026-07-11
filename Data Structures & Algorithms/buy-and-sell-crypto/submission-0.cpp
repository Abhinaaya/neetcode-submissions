class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price=prices[0];
        int max_profit=0;
        for(int i=1;i<prices.size();i++)
        {
            int curr=prices[i];
            int curr_profit=curr-min_price;
            max_profit=max(max_profit,curr_profit);
            min_price=min(min_price,curr);
        }
        return max_profit;
        
    }
};

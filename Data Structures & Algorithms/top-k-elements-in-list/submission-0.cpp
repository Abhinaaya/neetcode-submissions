class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        for(int num:nums)
        {
            map[num]++;
        }
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>>pq;
        for(auto &[num,count]:map)
        {
            pq.push({count,num});
            if(pq.size()>k) pq.pop();
        }
        vector <int> result;
        while(!pq.empty())
        {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
        
    }
};

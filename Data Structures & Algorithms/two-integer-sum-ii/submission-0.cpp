class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n=numbers.size();
        unordered_map<int,int>map;
        vector<int> result;
        for(int i=0;i<n;i++)
        {
            int k =target-numbers[i];
            if(map.find(k)!=map.end())
            {
                result.push_back(map[k]);
                result.push_back(i+1);
                return result;
            }
            map[numbers[i]]=i+1;
        }
        return result;

        
    }
};

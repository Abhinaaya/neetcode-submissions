class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

       int n=nums.size();
       unordered_set<int> s(nums.begin(),nums.end());
       int max_count=0;
       for(int num:s)
       {
        int current=num;
        int count =1;
        while(s.find(current+1)!=s.end())
        {
            current++;
            count++;
        }
        max_count=max(count,max_count);
       }
       return max_count;
    }
};

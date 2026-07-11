class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<int> st;
        int l=0;
        int r=0;
        int n=s.size();
        int max_length=0;
        for(int r=0;r<n;r++)
        {
            while(st.find(s[r])!=st.end())
            {
                st.erase(s[l]);
                l++;
            }
            
            st.insert(s[r]);
            max_length=max(max_length,r-l+1);
            
            
        }
        return max_length;

        
    }
};

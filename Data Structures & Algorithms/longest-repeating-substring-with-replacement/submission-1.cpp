class Solution {
public:
    int characterReplacement(string s, int k) {
        int max_length=0;
        int max_freq=0;
        int l=0;
        unordered_map<char,int> mp;
        for(int r=0;r<s.size();r++)
        {
            char curr_string=s[r];
            mp[curr_string]++;
            max_freq=max(max_freq,mp[curr_string]);
            int length=r-l+1;
            if((length-max_freq)>k)
            {
                char left_str=s[l];
                mp[left_str]--;
                l++;
                
            }
            max_length=max(max_length,r-l+1);

        }
        return max_length;
    }
};

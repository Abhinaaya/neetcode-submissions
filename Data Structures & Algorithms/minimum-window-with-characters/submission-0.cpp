class Solution {
public:
    string minWindow(string s, string t) {
        int l=0;
        int m=s.size();
        int n=t.size();
       
        if(m<n)
        {
            return "";
        }
        int min_l=INT_MAX;
        int r=0;
        vector<int>need(128,0),have(128,0);
        int req=0;
        for(char c:t)
        {
            if(need[c]==0)
            {
                req++;
            }
            need[c]++;
        }
        int formed=0;
        int start=0;
        while(r<m)
        {
            char c=s[r];
            have[c]++;
            if(need[c]>0 && need[c]==have[c])
            {
                formed++;
            }
            while(l<=r && formed==req)
            {
                if(min_l>r-l+1)
                {
                    min_l=r-l+1;
                    start=l;
                }
                char l_c=s[l];
                have[l_c]--;
                if(need[l_c]>0 && need[l_c]>have[l_c])
                {
                    formed--;
                }
                l++;
            }
            r++;
        }
        if(min_l==INT_MAX)
        {
            return "";
        }
        return s.substr(start,min_l);
        
    }
};

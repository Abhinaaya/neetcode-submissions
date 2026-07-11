class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> um;
        if(s.size()!=t.size())
        {
            return false;
        }
        string a=s;
        string b=t;
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        return (a==b);
        
    }
};

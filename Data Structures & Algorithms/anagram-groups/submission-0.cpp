class Solution {
public:
   
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       unordered_map<string,vector<string>> map;
       for(string s:strs)
       {
        string k=s;
        sort(k.begin(),k.end());
        map[k].push_back(s);
       }
       vector<vector<string>> result;
       for(auto &mp:map)
       {
        result.push_back(mp.second);
       }
       return result;

        
    }
};

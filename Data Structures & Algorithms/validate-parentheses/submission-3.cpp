class Solution {
public:
    bool isValid(string s) {
        int n=s.size();
        if(n%2==1)
        {
            return false;
        }
        stack<char>st;
        for(int i=0;i<n;i++)
        {
            char c=s[i];
            if(s[i]=='['||s[i]=='('||s[i]=='{')
            {
                st.push(s[i]);

            }
            else 
            {
                if(st.empty())
                {
                    return false;
                }
                char top = st.top();
                if ((c == ')' && top == '(') ||
                    (c == '}' && top == '{') ||
                    (c == ']' && top == '[')) 
                {
                    st.pop();
                }
                else
                {
                    return false;
                }
            }
        }
        if(st.empty())
        {
            return true;
        }
        return false;
        
    }
};

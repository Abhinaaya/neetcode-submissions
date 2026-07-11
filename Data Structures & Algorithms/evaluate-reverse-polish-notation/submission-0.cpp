class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>st;
        int n=tokens.size();
        for(string &c:tokens)
        {
            if(c=="+"|| c=="-" || c=="*" || c=="/")
            {
                int b=st.top();
                st.pop();
                int a=st.top();
                st.pop();
                int ans;
                if(c == "+") ans = a + b;
                else if(c == "-") ans = a - b;
                else if(c == "*") ans = a * b;
                else ans = a / b; 
                st.push(ans);
            }
            else
            {
                st.push(stoi(c));
            }
        }
        return st.top();
        
    }
};

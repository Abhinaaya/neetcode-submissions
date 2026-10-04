class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch not in "+-*/":
                st.append(int(ch))
            else:
                b=int(st.pop())
                a=int(st.pop())
                if ch=="+":
                    st.append(a+b)
                elif ch=="-":
                    st.append(a-b)
                elif ch=="*":
                    st.append(a*b)
                else:
                    st.append(int(float(a)/b))
        return st.pop()
        
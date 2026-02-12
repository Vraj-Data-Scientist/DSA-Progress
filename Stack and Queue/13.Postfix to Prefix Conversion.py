def PostfixToPrefix(s):
    n = len(s)
    i = 0
    st = []
    while (i < n):
        if ((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            st.append(s[i])
        else:
            t1 = st[-1]
            st.pop()
            t2 = st[-1]
            st.pop()
            st.append(s[i] + t2 + t1)
        i += 1
    return st[-1]

print(PostfixToPrefix('AB+CD-*'))
print(PostfixToPrefix('ABC/-AK/L-*'))
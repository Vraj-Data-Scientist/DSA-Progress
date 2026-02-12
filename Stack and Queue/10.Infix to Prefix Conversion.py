def prio(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixToPrefix(s):
    s = s[::-1]
    s = s.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    n = len(s)
    i = 0
    st = []
    ans = ''
    while (i < n):
        if ((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            ans = ans + s[i]
        elif (s[i] == '('):
            st.append(s[i])
        elif (s[i] == ')'):
            while (st and st[-1] != '('):
                ans += st[-1]
                st.pop()
            st.pop()
        else:
            if (s[i] == '^'):
                while (st and prio(s[i]) <= prio(st[-1])):
                    ans += st[-1]
                    st.pop()
            else:
                while(st and prio(s[i]) < prio(st[-1])):
                    ans += st[-1]
                    st.pop()
            st.append(s[i])
        i += 1
    while (st):
        ans += st[-1]
        st.pop()
    ans = ans[::-1]
    return ans

print(infixToPrefix('(a+b)*c-d+f'))
print(infixToPrefix("a*(b+c)/d"))

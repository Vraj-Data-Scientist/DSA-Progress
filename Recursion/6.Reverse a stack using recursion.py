def insert_at_bottom(st, key):
    if not st:
        st.append(key)
        return
    val = st.pop()
    insert_at_bottom(st, key)
    st.append(val)

def reverse_stack(st):
    if not st:
        return
    val = st.pop()
    reverse_stack(st)
    insert_at_bottom(st, val)

st1 = [1,5,2,7,0]
st2 = []
st3 = [1,1]
st4 = [9,8,7,6]
reverse_stack(st1)
reverse_stack(st2)
reverse_stack(st3)
reverse_stack(st4)
print(st1)
print(st2)
print(st3)
print(st4)
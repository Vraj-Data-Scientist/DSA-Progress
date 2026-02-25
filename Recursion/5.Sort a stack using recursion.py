def insert_in_sorted_list(list, key):
    list.append(key)
    n = len(list)
    i = n-2
    while (i >= 0 and list[i] > key):
        list[i+1] = list[i]
        i -= 1
    list[i+1] = key

l1 = [1,2,3,6]
insert_in_sorted_list(l1, 7)
print(l1)

def insert_in_sorted_stack(st, key):
    if (not st or st[-1] <= key):
        st.append(key)
        return
    value = st.pop()
    insert_in_sorted_stack(st, key)
    st.append(value)

st = [1,2,3,6]
insert_in_sorted_stack(st, 0)
print(st)

def sort_stack(st):
    if not st:
        return
    key = st.pop()
    sort_stack(st)
    insert_in_sorted_stack(st, key)

st1 = [1,5,2,7,0]
st2 = []
st3 = [1,1]
st4 = [9,8,7,6]
sort_stack(st1)
sort_stack(st2)
sort_stack(st3)
sort_stack(st4)
print(st1)
print(st2)
print(st3)
print(st4)

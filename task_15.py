a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
a_listed = list(set(a))
b_listed = list(set(b))
c_listed = []
for element in a_listed:
  if element in b_listed:
      c_listed.append(element)
print(c_listed)
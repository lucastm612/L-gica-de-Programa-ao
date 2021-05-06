x=int(input(" x =  "))
y=int(input(" y =  "))
mdc=1
if x>y:
    m = x
else:
    m = y
for i in range(1,m):
    if x%i==0 and y%i ==0:
        mdc=i
print (mdc)

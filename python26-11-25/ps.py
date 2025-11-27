#print even or odd
j=[10,11,12,13,14] #['even','odd','even','odd]
tem=[]
for x in j:
    if x%2==0:
        tem.append("even")
    else:
        tem.append("odd")
print(tem)
#list comprehension
res=[("even",x) if x%2==0 else ("odd",x) for x in j]
print(res)
#only odd
# res=[ for x in j if x%2==1 ("odd",x) ]
#
k=['abhi','python','django']
res=[(x,len(x)) for x in k if len(x)>=5]
print(res)
#print only extentions
b=["data.csv","repot.pdf","imag.png"]
for x in b:
    h=x.split(".")
    print(h[1])
#list comprehension print only extentions
res=[x.split(".")[1]for x in b]
print(res)
# list comprehension prime or not
k=[11,12,13]   #['prime','not prime']

# k=11
res=["prime" if all(x%y!=0   for y in range(2,x)) else "not prime"   for x in k]
print(res)
#3*3 matrix
res=[]
for x in range(1,4):
    tem=[]
    for y in range(1,4):
        tem.append(y)
    res.append(tem)
print(res)
#  list comprehension 3*3 matrix
res=[[y for x in range(1,4)] for y in range(1,4)]
print(res)
#remove zeros
k=[10,0,20,30]
res=[x for x in k if x!=0]
print(res)
#
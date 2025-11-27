#using genrater in tuple comprehension
h=(x for x in range(10))
# print(next(h))   #using genrater
for x in h:
    print(x)
#type conversion
h=tuple(x for x in range(1,10))
print(h[3])
#data type
j=[x for x in range(10)]
print(type(j))
#
res=tuple((x,x**3)for x in range(1,15) if x%2==1)
print(res)
#
j=10
for x in range(1,j):
    if x%2==0:
        print(x)
#tuple comprehension
res=tuple(x for x in range(1,j) if j%x==0)
print(res)
#even or odd
k=[10,11,12,13,14]
tem=[]
for x in k:
    if x%2==0:
        tem.append("even")
    else:
        tem.append('odd')
print(tem)
#list comprehension
res=[("even") if x%2==0 else("odd") for x in k]
print(res)
#prime or not
h=13
res=[x for x in range(1,h) if h%x==0]
if len(res)==1:
    print("prime")
else:
    print("not prime")
#print only owels in tuple comprehension
k='comprehension'
res=tuple(x for x in k if x in "AEIOUaeiou")
print(res)       
#set comprehension print numbers
res={x for x in range(1,10)}
print(res)
#
# res={x:x**2 for x in range (1,10)}
# print(res)
#
# res={{"s":x**2,"c":x**3} for x in range(1,5)}
# print(res)
#
# res={"a":10,"b":20,"c":30}
# tem={}
# for a,b in res.items():
#     tem[b]=a
# print(tem)
#
# res={"a":10,"b":20,"c":30}
#string convert into list
k="python fullstack developer".split()
res={x:len(x) for x in k if len(x)>6 }
print(res)
#dictionaery values in convert upper
k="python"
res={x.upper():ord(x.upper())for x in k}
print(res)
#
res={"even":[x for x in range(10) if x%2==0],"odd":[x for x in range(10) if x%2==1]}
print(res)
#
k=[10,11,12]
res={x:"even" if x%2==0 else "odd" for x in k}
print(res)
#alphabets
res={chr(x):x for x in range(65,90) if x%2==0}
print(res)
#
res={}
for x in range(65,91):
    res[chr(x)]=x
print(res)
#
k=[10,12,11,13]
res={for x in k if x%2==0}
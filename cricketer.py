#Input of Range 
n = int (input ("Enter number of elements: "))

#cricketer Name
a = []

#scores
s = []

#Input for list
for i in range (n):
    x = str(input("ENTER NAME:"))
    h = int(input("ENTER SCORES"))
    a.append(x)
    s.append(h)

m=s[0]

#comparing 
for z in range(n):
    if s[z]>m:
        m=s[z]
        pos=z

print("Name Of The Batsman With The Highest Score:",a[pos],",SCORE:", s[pos])
    

    

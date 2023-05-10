from matplotlib import pyplot as plt
a=input('enter the grade of CN:')
b=input('enter the grade of MCN:')
c=input('enter the grade of COA:')
d=input('enter the grade of FLAT:')
e=input('enter the grade of CON:')
x=[]
if a=='A' or a=='a':
    x.append(9)
elif a=='B' or a=='b':
    x.append(8)    
elif a=='C' or a=='c':
    x.append(7)
elif a=='D' or a=='d':
    x.append(6)
elif a=='e' or a=='E':
    x.append(5)
else:
    x.append(0)                
 
if b=='A' or b=='a':
    x.append(9)
elif b=='B' or b=='b':
    x.append(8)    
elif b=='C' or b=='c':
    x.append(7)
elif b=='D' or b=='d':
    x.append(6)
elif b=='e' or b=='E':
    x.append(5)
else:
    x.append(0)     
    
    
if c=='A' or c=='a':
    x.append(9)
elif c=='B' or c=='b':
    x.append(8)    
elif c=='C' or c=='c':
    x.append(7)
elif c=='D' or c=='d':
    x.append(6)
elif c=='e' or c=='E':
    x.append(5)
else:
    x.append(0)    
    
if d=='A' or d=='a':
    x.append(9)
elif d=='B' or d=='b':
    x.append(8)    
elif d=='C' or d=='c':
    x.append(7)
elif d=='D' or d=='d':
    x.append(6)
elif d=='e' or d=='E':
    x.append(5)
else:
    x.append(0)
    
if e=='A' or e=='a':
    x.append(9)
elif e=='B' or e=='b':
    x.append(8)    
elif e=='C' or e=='c':
    x.append(7)
elif e=='D' or e=='d':
    x.append(6)
elif e=='e' or e=='E':
    x.append(5)
else:
    x.append(0)             
    

print(x)   

plt.bar(['CN','MCN','COA','FLAT','CON'],x,color=['r','b','g','c','y'],width=0.4)
plt.title('STUDENT RESULT GRAPH')
plt.xlabel('SUBJECTS')
plt.ylabel('GCPC')
plt.legend()
plt.show() 
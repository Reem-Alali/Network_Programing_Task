import json
que = { }
#define a variable for the score
res = 0

num=1

b = open("questions.txt",'r')
que = json.load(b)
b.close()


name = input("Enter your name: ")
#display the questions
for i in que.keys():
    
    print("Question",num , ": ", i)
    a = input("The answer is ")
    
    if a == que[i]:
     res =   res + 1
     
    num = num + 1


result={name:res}
m= open("result.txt",'w')
final = json.dump(final,m)
m.close()
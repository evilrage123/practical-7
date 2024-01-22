# pelindrome number 
fh = open('pactical7.txt','w')
n= int(input('enter number: '))
sum=0
temp=n
while(n > 0):
    digit = (n%10)
    sum= sum*10 + digit
    n = n//10
    
if(sum == temp):
    fh.write('pelindrome')
else:
    fh.write('not pelindrome')
fh.close()
    
    
    
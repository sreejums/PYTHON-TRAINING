# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a=float(input())
b=float(input())
c=float(input())
if(a+b>c  and b+c>a and a+c>b):
     s=(a+b+c)/2
     area = math.sqrt(s*(s-a)*(s-b)*(s-c))
     print ('The area of the triangle  is : {:.2f}'.format(area))
else:
     print('Invalid Triangle')

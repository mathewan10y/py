'''format '''
a='cow'
b='moon'
print('the',a,'jumped over the',b)
print('the {} jumped over the {}'.format(a,b))
print('the {} jumped over the {}'.format(b,a))# order is changed
print('the {0} jumped over the {1}'.format(a,b))
print('the {1} jumped over the {0}'.format(a,b)) # positional
print('the {a} jumped over the {b}'.format(a='cow',b='moon'))
print('the {a} jumped over the {a}'.format(a='cow',b='moon'))#keyword 
name='mathew'

str=('hello my name is {:10}.nice to meet you').format(name)#leaves 10 spaces,  :>10 right alligned, :^10 center alligned
print(str)

pi=30980
l='{:.3f}'.format(pi) # takes three decimal places
print(l)

s='{:b}'.format(pi) # binary
t='{:o}'.format(pi) # octal
u='{:X}'.format(pi) # hexadecimal
v='{:,}'.format(pi) # adds comma in thousands place
m='{:E}'.format(pi)# scientific notation
print(s,t,u,v,m,sep='\n')
'''packs all the arguements into a list'''

def ad(*args):
    s=0
    for i in args:
        print(s)
        s+=i
    return s
print(ad(1,2,3,5))

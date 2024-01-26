''' **kwargs is a parameter that allows to pack all arguments into a dictionary so that a function can accept variable number of keys and values'''
def hello(**k):
    for key,value in k.items:
        print(value,end='')

hello('bro','hello','i','am','mathew')

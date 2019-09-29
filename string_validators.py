s = "qA2"
method=[str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]
results=[print(any([f(c) for c in s])) for f in method]

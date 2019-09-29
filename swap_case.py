def swap_case(s):
    arr=""
    for i in s:
        if i.isupper():
            arr+=i.lower()
        elif i.islower():
            arr+=i.upper()
        else:
            arr+=i
    return arr

print(swap_case('HackerRank.com presents "Pythonist 2".'))    

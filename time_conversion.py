def timeConversion(s):
    # Write your code here.
    if s[-2:]=="AM" and s[:2]=="12":
        print("00"+s[2:-2])
    elif s[-2:]=="AM":
        print(s[:-2])
    elif s[-2:]=="PM" and s[:2]=="12":
        print(s[:-2])
    else:
        print(str(int(s[:2])+12)+s[2:-2])

result=timeConversion("07:05:45PM")

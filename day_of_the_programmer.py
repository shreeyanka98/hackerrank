def dayOfProgrammer(year):
    if year>1918:
        if year%4==0:
            if year%100==0 and year%400!=0:
                print(f"13.09.{year}")
            else:
                print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")
    elif year==1918:
        print("26.09.1918")
    else:
        if year%4==0:
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")

dayOfProgrammer(2017)

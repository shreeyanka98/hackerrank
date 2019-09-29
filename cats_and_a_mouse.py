def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    print("Cat A" if a<b else "Cat B" if b<a else "Mouse C")

catAndMouse(1,2,3)
catAndMouse(1,3,2)

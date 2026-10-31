def score(x, y):
    d = (((x*x)+(y*y))**0.5)

    if 5<d<=10:
         return 1
    if 1<d<=5:
        return 5
    if 0<=d<=1:
        return 10
    return 0
         
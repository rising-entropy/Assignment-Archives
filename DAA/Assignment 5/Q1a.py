mid = []

# The quadrant in which the point lies
def whichQuadrant(p):
    if p[0] >= 0 and p[1] >= 0:
        return 1
    if p[0] <= 0 and p[0] >= 0:
        return 2
    if p[0] <= 0 and p[0] <= 0:
        return 3
    return 4

# Checks whether the line is crossing the polygon
def orientation(a, b, c):
    ori = (b[1] - a[1])*(c[0]-b[0]) - (c[1]-b[1])*(b[0]-a[0])
    # perfect overlap
    if ori == 0:
        return 0
    # outside
    if ori > 0:
        return 1
    return -1

# compare function for sorting
def compare(p1, p2):
    global mid
    p = (p1[0]-mid[0], p1[1]-mid[1])
    q = (p2[0]-mid[0], p2[1]-mid[1])

    uno = whichQuadrant(p)
    dos = whichQuadrant(q)

    if uno == dos:
        return 0
    if uno < dos:
        return -1
    return 1

# Finds upper tangent of two polygons 'a' and 'b'
# represented as two vectors.
def merger(a, b):
    # points in poly 1
    n1 = len(a)
    # points in poly 2
    n2 = len(b)

    ia = 0
    ib = 0

    for i in range(1, n1):
        if a[i][0] > a[ia][0]:
            ia = i

    for i in range(1, n2):
        if b[i][0] < b[ib][0]:
            ib=i

    # upper tangent
    inda = ia
    indb = ib
    done = False

    while(not done):
        done = True
        while(orientation(b[indb], a[inda], a[(inda+1)%n1]) >= 0):
            inda = (inda+1)%n1
        while(orientation(a[inda], b[indb], b[(n2+indb-1)%n2]) <=0):
            indb = (n2+indb-1)%n2
            done = False

    uppera = inda
    upperb = indb
    inda = ia
    indb = ib
    done = False
    g = 0
    # lower tangent
    while(not done):
        done = True
        while (orientation(a[inda], b[indb], b[(indb+1)%n2])>=0):
            indb=(indb+1)%n2
        while (orientation(b[indb], a[inda], a[(n1+inda-1)%n1])<=0):
            inda=(n1+inda-1)%n1
            done=0

    lowera = inda
    lowerb = indb
    ret = []
    ind = uppera
    ret.append(a[uppera])
    while (ind != lowera):
        ind = (ind+1)%n1
        ret.append(a[ind])
    
    ind = lowerb
    ret.append(b[lowerb])
    while(ind != upperb):
        ind = (ind+1)%n2
        ret.append(b[ind])
    return ret

# Brute force algorithm to find convex hull for a set
# of less than 6 points
def bruteHull(a):
    # Take any pair of points from the set and check
    # whether it is the edge of the convex hull or not.
    # if all the remaining points are on the same side
    # of the line then the line is the edge of convex
    # hull otherwise not

    s = []

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            x1 = a[i][0]
            x2 = a[j][0]
            y1 = a[i][1]
            y2 = a[j][1]
  
            a1 = y1-y2
            b1 = x2-x1
            c1 = x1*y2-y1*x2
            pos = 0
            neg = 0
            for k in range(len(a)):
                if (a1*a[k][0]+b1*a[k][1]+c1 <= 0):
                    neg += 1
                if (a1*a[k][0]+b1*a[k][1]+c1 >= 0):
                    pos += 1
            if (pos == len(a) or neg == len(a)):
                s.append(a[i]);
                s.append(a[j]);
            

    ret = []
    for e in s:
        ret.append(e)
    
    global mid
    mid = [0, 0]

    n = len(ret)

    for i in range(n):
        mid[0] += ret[i][0]
        mid[1] += ret[i][1]
        ret[i][0] *= n
        ret[i][1] *= n
    
    # ret = sorted(ret, key=compare)
    ret = sorted(ret, key=lambda x: x[0])
    for i in range(n):
        ret[i] = [ret[i][0]/n, ret[i][1]/n]

    return ret

def divide(a):
    # If the number of points is less than 6 then the
    # function uses the brute algorithm to find the
    # convex hull
    if len(a) <= 5:
        return bruteHull(a);

    # left contains the left half points
    # right contains the right half points
    left = []
    right = []

    for i in range(len(a)//2):
        left.append(a[i])
    for i in range(len(a)//2, len(a)):
        right.append(a[i])
    
    left_hull = divide(left)
    right_hull = divide(right)

    return merger(left_hull, right_hull)

points = [[1, 4], [4, 4], [7, 4], [1, 3], [3, 3], [6, 3], 
            [8, 3], [1, 2], [3, 2], [5, 2], [7, 2], [9, 2], [2, 1], 
            [4, 1], [6, 1], [8, 1]]

n = len(points)

# sort wrt x-co-ordinates
points = sorted(points, key=lambda x: x[0])

ans = divide(points)

print(ans)
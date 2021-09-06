
listOfBuildings = [[0,2,3],[2,5,3]]

def update_output(output, x, y):
    # Update the final output with the new element.
    # if skyline change is not vertical - add the new point
    if not output or output[-1][0] != x:
        output.append([x, y])
    # if skyline change is vertical - update the last point
    else:
        output[-1][1] = y

def append_skyline(output, p, lst, n, y, curr_y):
    # Append the rest of the skyline elements with indice (p, n) to the final output.
    while p < n: 
        x, y = lst[p]
        p += 1
        if curr_y != y:
            update_output(output, x, y)
            curr_y = y

def mergeSkylines(left, right):
    n_l = len(left)
    n_r = len(right)
    p_l = p_r = 0
    curr_y  = left_y = right_y = 0
    output = []
        
    # while we're in the region where both skylines are present
    while p_l < n_l and p_r < n_r:
        point_l, point_r = left[p_l], right[p_r]
        # pick up the smallest x
        if point_l[0] < point_r[0]: 
            x, left_y = point_l
            p_l += 1
        else: 
            x, right_y = point_r 
            p_r += 1
        # max height (i.e. y) between both skylines
        max_y = max(left_y, right_y)
        # if there is a skyline change
        if curr_y != max_y:
            update_output(output, x, max_y)
            curr_y = max_y

    # there is only left skyline
    append_skyline(output, p_l, left, n_l, left_y, curr_y)

    # there is only right skyline
    append_skyline(output, p_r, right, n_r, right_y, curr_y)
            
    return output

def getSkyline(buildings):
    n = len(buildings)

    # Base Case
    if n == 0:
        return []
    if n == 1:
        xStart, xEnd, y = buildings[0]
        return [[xStart, y], [xEnd, 0]]

    # For 2 or more buildings, we recurse to 2 subproblems
    leftSkyline = getSkyline(buildings[:n//2])
    rightSkyline = getSkyline(buildings[n//2:])

    return mergeSkylines(leftSkyline, rightSkyline)

print(getSkyline(listOfBuildings))

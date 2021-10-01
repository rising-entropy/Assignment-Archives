import sys
 
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
 
    def find(self, s):
        if s == self.parent[s]:
            return s
        self.parent[s] = self.find(self.parent[s])
        return self.parent[s]

    def merge(self, u, v):
        self.parent[v] = u
 
def cmp(a):
    return a['profit']
 
def maxDeadline(jobs, n):
    ans = - sys.maxsize - 1
    for i in range(n):
        ans = max(ans, jobs[i]['deadline'])
    return ans
 
def printScheduling(jobs, n):
    jobs = sorted(jobs, key = cmp, reverse = True)
 
    # create a disjoint set data structure
    max_deadline = maxDeadline(jobs, n)
    ds = DisjointSet(max_deadline)
    maximisedProfit = 0
    for i in range(n):
        # find maximum available free slot 
        available_slot = ds.find(jobs[i]['deadline'])
        if available_slot > 0:
            ds.merge(ds.find(available_slot - 1),
                             available_slot)
            print(jobs[i]['id'], end = " ")
            maximisedProfit += jobs[i]['profit']
    
    return maximisedProfit

if __name__ == "__main__":
    jobs = [{
        "id": "a",
        "deadline": 2,
        "profit": 100
    },
    {
        "id": "b",
        "deadline": 1,
        "profit": 19
    },
    {
        "id": "c",
        "deadline": 2,
        "profit": 27
    },
    {
        "id": "d",
        "deadline": 1,
        "profit": 25
    },
    {
        "id": "e",
        "deadline": 3,
        "profit": 15
    }]
    n = len(jobs)
    print("Job Schedule Sequence:")
    maxProfit = printScheduling(jobs, n)
    print("\nMaximised Profit: "+str(maxProfit))
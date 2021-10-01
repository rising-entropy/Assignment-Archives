def printJobScheduling(jobs, t):
  
    # length of the list
    n = len(jobs)
  
    # Reverse sort profit
    jobs = sorted(jobs, key=lambda k: (-k['profit']))
  
    # Free slots
    result = [False] * t
  
    # Sequene of the Jobs
    res = ['-1'] * t

    maximisedProfit = 0

    for job in jobs:
        for j in range(min(t-1, job["deadline"] -1), -1, -1):
            if result[j] is False:
                result[j] = True
                res[j] = job["id"]
                maximisedProfit += job["profit"]
                break

    return res, maximisedProfit

jobs = [
    {
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
    },
]

deadlines = []
for job in jobs:
    deadlines.append(job["deadline"])
maxiDeadline = max(deadlines)

result, maxProfit = printJobScheduling(jobs, maxiDeadline)

print("Job Schedule Sequence:", end=' ')
print(result)

print("Maximised Profit: "+str(maxProfit))
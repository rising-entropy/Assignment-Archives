
# job sequence from a given array
# of jobs with deadlines and profits
  
# function to schedule the jobs take 2
# arguments array and no of jobs to schedule
  
  
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


n1 = 7
profits = [3,5,20,18,1,6,30]
deadlines = [1,3,4,3,2,1,2]
jobs = []
maxiDeadline = max(deadlines)

for i in range(n1):
    temp = {
        "id": i+1,
        "profit": profits[i],
        "deadline": deadlines[i],
        "taken": False
    }
    jobs.append(temp)

result, maxProfit = printJobScheduling(jobs, maxiDeadline)

print("Job Schedule Sequence:", end=' ')
print(result)

print("Maximised Profit: "+str(maxProfit))
# Generate table of feasible,proceesing sequencing , profit

# We build a list of id, deadline and profit from the array input.
# First step of determining Job Scheduling

n1 = 7
profits = [3,5,20,18,1,6,30]
deadlines = [1,3,4,3,2,1,2]
jobs = []

for i in range(n1):
    temp = {
        "id": i+1,
        "profit": profits[i],
        "deadline": deadlines[i],
        "taken": False
    }
    jobs.append(temp)

# We also sort the jobs based
jobs = sorted(jobs, key=lambda k: (-k['profit']))

# Retrieve all jobs
for job in jobs:
    print("id - "+str(job["id"]))
    print("profit - "+str(job["profit"]))
    print("deadline - "+str(job["deadline"]))
    print()
class Job:
    def __init__(self,id,deadline,profit) -> None:
        self.id = id
        self.deadline = deadline
        self.profit = profit


def Jobscheduling(jobs):
    # jobs.sort(key = lambda x: x.profit, reverse = True)

    # total_profit = 0
    # cnt = 0
    # maxdeadline = max(job.deadline for job in jobs)
    # hashmpp = [-1]*(maxdeadline+1)

    # for i in range(len(jobs)):
    #     for j in range(jobs[i].deadline,0,-1):
    #         if hashmpp[j] == -1:
    #             cnt += 1
    #             hashmpp[j] = jobs[i].id
    #             total_profit += jobs[i].profit
    #             break
    # return [total_profit,cnt]
    jobs.sort(key = lambda x: x.profit,reverse = True)
    totalprofit = 0
    cnt = 0
    maxdeadline = max(job.deadline for job in jobs)
    mpp = [-1]*(maxdeadline+1)

    for i in range(len(jobs)):
        for j in range(jobs[i].deadline,0,-1):
            if mpp[j] == -1:
                cnt += 1
                mpp[j] = jobs[i].id
                totalprofit += jobs[i].profit
                break
    return [totalprofit,cnt]





n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    id = i + 1
    deadline = int(input(f"Enter deadline for job {i+1}: "))
    profit = int(input(f"Enter profit for job {i+1}: "))
    jobs.append(Job(id, deadline, profit))

ans = Jobscheduling(jobs)
print(ans)

A=[]
def iterative_activity_selector(activities,k,m):
    A.append(activities[0])
    m=0
    for i in range(1,len(activities)):
        
        if(activities[i][1]<activities[m][2]):
            continue
        else:
            A.append(activities[i])
            m=i

ids=[0,1,2,3,4,5,6,7,8,9,10]
start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
activities=list(zip(ids,start_times,finish_times))
activities.sort(key=lambda x:x[2])
iterative_activity_selector(activities,0,0)
print(A)
A=[]
def recursive_activity_selector(activities,m,n):
    k=n+1
    if(k>=len(activities)):
        return
    if(activities[m][2]>activities[k][1]):
        recursive_activity_selector(activities,m,k)
    else:
    
        A.append(activities[k])
        m=k
        recursive_activity_selector(activities,m,k)

ids=[0,1,2,3,4,5,6,7,8,9,10]
start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
activities=list(zip(ids,start_times,finish_times))
activities.sort(key=lambda x:x[2])
A.append(activities[0])
recursive_activity_selector(activities,0,0)
print(A)

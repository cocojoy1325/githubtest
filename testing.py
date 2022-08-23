import datetime
def my_range(start,end):
    current = start
    while current < end:
        yield current
        current +=1

nums = my_range(1,5)

print(next(nums))

list1 = [1,2,3]

list1.append({'name' : 'aman' , "id" : 70})

print(list1)

print(datetime.date(2020,4,1))

print(datetime.datetime(2020, 9, 18, 0, 57))









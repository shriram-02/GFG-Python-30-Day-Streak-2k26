# declare the variable count here
count = 0

def utility():
    # access the global variable count
    global count  
    # increases the value of count by 1
    count += 1
    print(count, end=" ")

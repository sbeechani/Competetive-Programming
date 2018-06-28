def contains(ordered_list, number):

    # Check if an integer is present in the list
    mini = 0
    maxi = len(ordered_list)-1
    while(maxi>=mini):
        mid = int((maxi+mini)/2)
        if(number>ordered_list[mid]):
            mini=mid+1
            
        elif(number<ordered_list[mid]):
            maxi=mid-1
        else:
            return True
    

    return False

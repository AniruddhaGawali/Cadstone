

def BinarySearch(list1,start,end,num):
    mid = (start + end)//2
    # for i in range(0,len(list1)):
    if(num == list1[mid]):
            return mid
    elif(num > list1[mid]):
        start = mid + 1
        return BinarySearch(list1,mid+1,end,num)
    elif(num < list1[mid]):
        end = mid - 1
        return BinarySearch(list1,start,mid-1,num)
    else:
          return -1
    

def main():
    list1= [1,2,3,4,5]
    num = int(input("Enter the number to be found: "))
    res = BinarySearch(list1,0,len(list1),num)
    if(res == -1):
            print("The element is not found")
    else:
            print(f"The number is found at {res}")    

if __name__ == "__main__":
    main()
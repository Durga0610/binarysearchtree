n=int(input("Enter the element:"))
lst=[]
flag=0
for i in range(n):
    data=int(input("Enter the value:"))
    lst.append(data)
search=int(input("Enter the search element:"))
low=0
high=n-1
while(low<high):
    mid=(low+high)//2
    if(lst[mid]==search):
       flag=mid
       break
    elif(search>lst[mid]):
        low=mid+1
    else:
        high=mid-1
if(flag==0):
    print("Element not found")
else:
    print(f"Element present at index  {flag}")
       

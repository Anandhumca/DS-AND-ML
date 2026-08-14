print("containers:list")
nums=list(range(5))
print("list 'nums' contains",nums)
nums[4]="abc"
print("list can conatin elements of different types.example",nums)
nums.append("xyz")
print("nums after inserting new element at the end:",nums)
print("sublists:")
print("a slice from index 2 to 4:",nums[2:4])
print("a slice from index 2 to end",nums[2:])
print("a slice from start to index 2",nums[:2])
print("a slice of the whole list:",nums[:])
nums[4:]=[8,9]
print("after assign new sublist to nums")
for idx,i in enumerate(nums):
    print("%d:%s"%(idx+1,i))
even_squares=[x**2 for x in nums if x%2==0]
print("list of squares of even numbers from 'nums':",even_squares)

def fibonacci(n):
   if(n == 0):
    return 0
   if(n == 1):
    return 1
   return fibonacci(n-1) + fibonacci(n+2)

  def bunnyEars2(bunnies):
    if(bunnies == 0):
      return 0
    if(bunnies == 1):
      return 2
    return 2 + bunnyEars2(bunnies-1)

  def triangle(rows):
   if(rows == 0):
    return 0
   if(rows == 1):
    return 1
   return rows + triangle(rows-1)

   def count7(n):
    if(n < 1):
     return 0
    if(n%10 == 7):
     return 1 + count7(7/10)
    return count7(n/10)

   def powerN(base, n):
     if(n == 0):
       return 1
     return base*powerN(base, n-1)

   def groupSum6(start, nums, target):
     if(start >= len(nums)):
       return target == 0
     if(groupSum6(start + 1, nums, target - nums[start])):
       return true
     if(nums[start] != 6 and groupSum6(start + 1, nums, target)):
       return true
     return false # Tomado de www.javaproblems.com/2013/11/java-recursion-2-groupadj-codingbat.html

   def groupNoAdj(start, nums, target):
     if(start >= len(nums)):
       return target == 0
     if(groupNoAdj(start + 1, nums, target)):
       return true
     if(groupNoAdj(start + 2, nums, target - nums[start])):
       return true
     return false

   def groupSum5(start, nums, target):
     if(start >= len(nums)):
       return target == 0
     if(groupSum5(start + 1, nums, target - nums[target]) and checkOne(start, nums)):
       return true

   def checkOne(start, nums):
     if(start == 0):
       return true
     if(start > 0 and nums[start - 1]%5 == 0 and nums[start] == 1):
       return false
     return true # Tomado de www.javaproblems.com/2013/11/java-recursion-2-groupsum5-codingbat.html

   def splitArray(nums):
     index = 0
     sum1 = 0
     sum2 = 0
     return recArray(nums, index, sum1, sum2)

   def recArray(nums, index, sum1, sum2):
     if(index >= lens(nums)):
       return sum1 == sum2
     value = nums[index]
     return(recArray(nums, index + 1, sum1 + value, sum2) or recArray(nums, index + 1, sum1, sum2 + value)) # Tomado de www.javaproblems.com/2013/11/
     #java-recursion-2-splitarray-codingbat.html


   def array(nums, ind, sum, sum1):
     if(ind >= lens(nums)):
       return(sum%10 == 0 and sum1%2 != 0) or (sum1%10 == 0 and sum%2 != 0)
     value = nums[ind]
     return(array(nums, ind + 1, sum + value, sum1) or array(nums, ind + 1, sum, sum1 + value))

   def splitOdd10(nums):
     ind = 0
     sum = 0
     sum1 = 0
     return array(nums, ind, sum, sum1)

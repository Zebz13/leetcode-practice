class Solution:

    def find_primes_under(self, num: int) -> list:
        prime_list= [0,0]
        for i in range(2,num):
            flag = 0
            for j in range(2,int(i**0.5)+1):
                if i%j == 0:
                    flag = 1
                    prime_list.append(prime_list[i-1])
                    break
            if not flag:
                prime_list.append(i)
        return prime_list

    def primeSubOperation(self, nums: list[int]) -> bool:
        prime_list = self.find_primes_under(max(nums))
        prev_element = 0
        for count,num in enumerate(nums):
            index_prime = num-prev_element-1
            # print((num - prime_list[index_prime])< prev_element)
            if(not (num - prime_list[index_prime]) > prev_element):
                return False
            else:
                prev_element = num - prime_list[index_prime]
        return True
                
sol = Solution()
print(sol.primeSubOperation([5,8,3]))



# class Solution:
#     def find_primes_under(self, num: int) -> list:
#         prime_list= []
#         for i in range(2,num):
#             flag = 0
#             for j in range(2,int(i/2)+1):
#                 if i%j == 0:
#                     flag = 1
#                     break
#             if not flag:
#                 prime_list.append(i)
#         return prime_list

#     def primeSubOperation(self, nums: list[int]) -> bool:
#         prime_list = self.find_primes_under(1000)
#         for count,num in enumerate(nums[:-1]):
#             if(count !=0):
#                 lesser_primes = [i for i in prime_list if i < num and num-nums[count-1]>i]
#                 if(not lesser_primes):
#                    continue
#                 else:
#                     nums[count] = nums[count] - lesser_primes[-1]
#             elif( count == 0):
#                 lesser_primes = [i for i in prime_list if i < num]
#                 if(not lesser_primes):
#                    continue
#                 else:
#                     nums[count] = nums[count] - lesser_primes[-1]
#             # print(nums)
#         for count,num in enumerate(nums[:-1]):
#             if(not(num<nums[count+1])):
#                 return False
#         return True
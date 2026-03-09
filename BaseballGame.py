# This is a Baseball game command tool.
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.record=[] # Create the list but do not save any information in it
        for op in operations: # We need to go through every command that comes to the list, so we use a for loop.
            if op == "+": # If you press the “+” key, add the result to the end of the list after adding the last two items in the list.  
                self.record.append(self.record[-1] + self.record[-2])
                print(self.record)
            elif op == "D": #If you press the “D” key, multiply the last item in the list by two and then add the result to the end of the list. 
                self.record.append(self.record[-1]*2)
                print(self.record)
            elif op == "C": # If you press the “C” key, remove the last item from the list.
                self.record.pop()
                print(self.record)
            else: #If it is not one of these, it should now be a number; add these values to the list as well.
                self.record.append(int(op)) # Attention! Since the numbers will be in string format, you must convert them to integers.
                print(self.record)

        return sum(self.record)

'''
Notes:
1) All print statements are included solely to monitor the process. They are not required in your code.
2) The sum() function is used because Python is employed. If you prefer, you can sum the entire list using a for loop.
3) Additionally, the list must be summed after all operations are complete, hence this rule has been applied.
4) If you want to solve this coding challenge, you can visit the LeetCode website and look at the Baseball Game page.
'''

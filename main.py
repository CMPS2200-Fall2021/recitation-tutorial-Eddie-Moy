def sum_of_squares(a):
   sum = 0
   for i in range(len(a)):
      toAdd = a[i]**2
      sum += toAdd
   return sum


	
def test_one():
   assert sum_of_squares([1,2,3]) == 14

def test_two():
   assert sum_of_squares([4,4,4]) == 48

test_one()
test_two()

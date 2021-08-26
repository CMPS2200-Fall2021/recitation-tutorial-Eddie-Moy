def sum_of_squares(a):
	sum = 0
	for i in range(a + 1):
		mult = i * i
		sum += mult

def test_one():
    assert sum_of_squares([1,2,3]) == 14

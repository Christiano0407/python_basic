from test.main import sum


def test_sum():
  assert sum(5, 5) == 10
  assert sum(7, 4) == 11
  assert sum(-5, -5) == -10
  assert sum(0, 0) == 0
  #assert sum(-1, 2) == 0 # = Assertion Error = 


if __name__ == "__main__":
  print("Previous Test...") 
  test_sum()
  print("All Tests Passed...:)") 
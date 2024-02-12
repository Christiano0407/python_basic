######
#! === Array (Methods and Behavior or Conduct) (Init & Limit) ===
######
class Array: 
  def __init__(self, capacity, array_value="None"):
    self.items = list()
    for i in range(capacity):
      #value = [fill_value] * capacity
      self.items.append(array_value)
      
  # === Methods Privates ===
  def __len__(self):
    return len(self.items)
  
  def __str__(self) -> str:
    #return str(self.items)
    return 'str: [' + ', '.join(str(item) for item in self.items) + ']'
  
  def __iter__(self): 
    return iter(self.items)
  
  def __getitem__(self, index): 
    return self.items[index]
  
  def __setitem__(self, index, new_item): 
    self.items[index] = new_item
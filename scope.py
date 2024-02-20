name = "Dave"
count = 1

def another():
  color = "blue"
  global count 
  count += 1
  print(count)
  
  def greeting(name):
    nonlocal color
    color = "red"
    print(name)
    print(color)

  greeting("Dave")

another()


import os
# r = Read
# a = Append
# w = Write
# x = create

# Read - error if files doesn't exist

f = open("names.txt", "r")
#print(f.read())
#print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
  print(line)


f.close()

try:
  f = open("names.txt")
  print(f.read())
except:
  print("File doesn't exist")
finally:
  f.close()

#append - creates file if not exists
  
f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt", "r")
print(f.read())
f.close()

#Write (Overwrites)

f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()

#Two ways to create a new file

#Opens a file for writing, creates the file if it does not exist
f =open("name_list.txt", "w")
f.close()
#creates the specified file, but returns an error if the files exists

if not os.path.exists("dave.txt"):
  f = open("dave.txt", "x")
  f.close()

# Delete a file
  
# avoid an error if it doesn't exists
if os.path.exists("dave.txt"):
  os.remove("dave.txt")
else: 
  print("The file doesn't exist")

with open("more_names.txt") as f:
  content = f.read()

with open("names.txt", "w") as f:
  f.write(content)

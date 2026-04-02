"""3. Grocery List Manager
A user wants to save grocery items in a file grocery.txt. Write a Python program that
takes multiple items from the user and writes them into the file, with each item on a
new line."""
items=['Milk','Powder','Lip Balm','Veggies']
file=open("grocery.txt",'w')
for i in items:
    file.write(i+"\n")
file.close()
file=open("grocery.txt",'r')
data=file.read()
print(data)
file.close()
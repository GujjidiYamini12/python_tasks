"""2. Notes Reader Program
A student stores daily notes in a file called notes.txt. Write a program that opens the
file, reads all the contents, and displays them on the screen.
"""
file=open("notes.txt","w")
data=file.write("Hello, How are you?\nHow is your doing?\nHappy to meet you")
file.close()
file=open("notes.txt","r")
print(file.read())
#print(file.readlines())
#print(file.readline())
file.close()
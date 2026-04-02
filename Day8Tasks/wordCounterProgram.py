"""5. Word Counter Program
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results."""
with open("article.txt","w") as file:
    data=file.write("Hello\nHow are You?")
with open("article.txt","r") as file:
    data=file.read()
    charact_count=len(data)
    word_count=len(data.split())
    lines_count=data.count("\n")+1
    print(f"data available:\n{data}\nCharacters are: {charact_count}\nWords are: {word_count}\nlines are: {lines_count}")
    
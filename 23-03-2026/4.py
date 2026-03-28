'''Take a sentence as input and print it in uppercase. '''
sentence=input()
#print(sentence.upper())
new_sen=""
for i in sentence:

    if ord(i)>=97:
        i=chr(ord(i)-32)
    else:
        i=i
    new_sen=new_sen+i
print(new_sen)
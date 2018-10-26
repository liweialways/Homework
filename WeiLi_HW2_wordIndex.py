
# coding: utf-8

# In[1]:


"""
Homework 2
program: WeiLi_homework2_wordIndex.py
student: Wei Li

present the words' positions in a .txt file:
1. the inputs is:
    the .txt file name
    
2. output is:
    title: Word and the corresponding positions in File + fileName +  are \n
    contents: the words in alphabetic order and the positions of them
    
3. the positions of words start from 1.
    
"""
# open and read file, save it in lower cases and split it by space:
fileName = input("Enter the file name: ")
file = open(fileName, 'r')
text = file.read().lower().split()

# the punctuation marks are:
marks = ('?', '.', ';', '!', ':', ',')

# remove the punctuation marks:
emp = []
for m in marks:
    for n in text:
        split = n.split(m)
        for l in split:
            if l != '':
                emp.append(l)
    text = emp
    emp = []
    
# print the title
print('Word and the corresponding positions in File ' + fileName + " are \n" )

# construct the dictionary, sort keys, print the words alphabetically with their positions:
aDic = {}
for t in range(len(text)):
    if text[t] not in aDic:
        aDic[text[t]] = [t+1]
    elif text[t] in aDic:
        aDic[text[t]].append(t+1)
keys = list(aDic.keys())
keys.sort()
for q in keys:
    index = aDic[q]
    # print bolded characters:
    class color:
        BOLD = '\033[1m'
        END = '\033[0m'
    print(color.BOLD + q + color.END + ':'+ str(index))


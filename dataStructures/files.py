# 
# ! using open()
# * handle = open(filename, mode) returns a handle use to manipulate the file
# * filename is a string
# * mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write  to the file
# * the new line character is \n .

'''
Write a program that prompts for a file name, then opens that file and reads 
through the file, and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
'''
fname=input('Enter the file name:')
try:
    fhand= open(fname,'r')
    content= fhand.read()
    content=content.strip()
    content=content.upper()
except:
    print('File cannot be opened: ', fname)
    quit()

print(content)

'''
Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the 
average of those values and produce an output as shown below. Do not use the sum() function or 
a variable named sum in your solution.
'''
fname = input("Enter file name: ")
fh = open(fname)
result=0.0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line=line.strip()
    count=count+1
    result=result+float(line[line.find('.'):])
    #print(result)
print('Average spam confidence:',result/count)

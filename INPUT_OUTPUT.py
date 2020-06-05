f = open('inputFile.txt', 'r')
passfile = open('passfile.txt', 'w')
failfile = open('failfile.txt', 'w')
count = 0
for i in f:
    line = i.split()
    if(line[2] == 'P'):
        print(str(count)+':'+i)
        passfile.write(i)
        count += 1
    else:
        failfile.write(i)
# print(f.read())
f.close()
passfile.close()
failfile.close()

# IN THIS WE HAVE WORKED ON CREATING NEW FILES BY WRITING IT! AND DISTINGUISHING THE CATEGORY AS PASS 
# AND FAIL INTO 2 DIFFERENT FILES

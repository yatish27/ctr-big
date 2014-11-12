import time

inp=open('/Users/saurabh/Documents/SampleData.csv')

#inp=open('SampleData.csv')

column=[set() for p in range(40)]
start_time = time.time()
x=inp.readline()
end_time=time.time()

print "time to read one line is: "+str(end_time-start_time)+" seconds"
no_of_records=4000000
print "time to read "+str(no_of_records)+" lines is: "+str((end_time-start_time)*no_of_records)+" seconds"

for line in inp:
    words=line.split('\t')
    for i in range(40):
        if(words[i] not in column[i]):
            column[i].add(words[i])
            
            
out=open('/Users/saurabh/Documents/FilteredData.txt','w')            
#out=open('FilteredData.txt','w') 
for j in range(40):
    out.write('Unique Value Set for coloumn '+str(j)+'::')
    out.write(str(column[j]))
    out.write('\n') 
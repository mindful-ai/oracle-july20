# OBJECTIVE:
# Calculate average and ranks
# Write a new csv file

# Reporting functions

def genReport(dd):
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for regid in dd.keys():
        name = dd[regid]['name']
        age  = dd[regid]['age']
        regid = dd[regid]['regid']
        phy = dd[regid]['phy']
        chem = dd[regid]['chem']
        math = dd[regid]['math']
        bio = dd[regid]['bio']
        avg = dd[regid]['avg']
        rank = dd[regid]['rank']
        print(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
    print(dottedline)

def write2file(dd, path):
    pass



# Read the csv file as a text file

path = r"C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\case\students.csv"
f = open(path)
content = f.readlines()
f.close()

#print(content)
#print('-'*60+'> STEP - 1')

# ------------------------ csv file is read and its content is available for further processing

# Read the coloums --> name,age,regid,phy,chem,math,bio,avg,rank
# Read a row --> Vijay,14,HPE001,99,98,97,96,0,0
# Construct a dictionary out of the column and the row
# Add that dictionary to the main dictionry that represents the class
# Repeat this process for all the entries in the csv file

classdict = {}

coldata  = content[0]
columns  = [item.strip() for item in coldata.split(',')]
for rowdata in content[1:]:
    #rowdata  = content[1]
    rows     = [item.strip() for item in rowdata.split(',')]
    studdict = dict(zip(columns, rows))
    classdict.setdefault(studdict['regid'], studdict)

#print(classdict)
#print('-'*60+'> STEP - 2')

# ------------------------- csv data is in the form of a dictionary

# Access the dictionary iteratively and calculate the average marks and
# update in the dictionary

for regid in classdict.keys():
    # sum_of_subjmarks = classdict[regid]['phy'] + classdict[regid]['chem'] + ...
    sum_of_subjmarks = 0
    for key in ['phy', 'chem', 'math', 'bio']:
        sum_of_subjmarks += int(classdict[regid][key])
    classdict[regid]['avg'] = sum_of_subjmarks / 4


#print(classdict)
#print('-'*60+'> STEP - 3')


# ------------------------- dictionary updated with average data

# Calculate the rank
# collect all the averages -> into a list
# arrange the averages in descending order
# iterate the entire dictionary and update the rank based on the descending
# order of averages

avgs = [classdict[regid]['avg'] for regid in classdict.keys()]

# avgs = list(set(avgs))   # Why is this needed?

avgs.sort(reverse=True)

print('AVERAGES: ', avgs)

rank = 1
for avg in avgs:
    for regid in classdict.keys():
        if(classdict[regid]['avg'] == avg):
            classdict[regid]['rank'] = rank
    rank += 1

#print(classdict)
#print('-'*60+'> STEP - 4')

# ------------------------- dictionary updated with rank data

# Re-write the csv file

path = r"C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\case\students_updated.csv"
f = open(path, 'w')

f.write(coldata)

for regid in classdict.keys():
    r = list(zip(*classdict[regid].items()))
    rowdata = ','.join([str(item) for item in r[1]]) + '\n'
    f.write(rowdata)


f.close()

#print('File written: students_updated2.csv')
#print('-'*60+'> STEP - 5')

genReport(classdict)


# ------------------------- resultant csv file is now ready with averages and ranks updated

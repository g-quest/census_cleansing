
f = open('urpop0090.txt','r')
file = f.read()

# index each line in a list as a string
fileSplit = file.split('\n')

# clean out data
cleanList = []
for element in fileSplit:
    if element.endswith('%'):
        element = element.replace(' r ',' ')
        element = element.replace(' *2 ',' ')
        if ('Division' in element) or ('Region' in element) or ('UNITED STATES' in element):
            pass
        else:
            cleanList.append(element)
      
# split fields of each line into elements in a list
splitList = []
for element in cleanList:
    
    element = element.split()
    
    # make two-worded states into a single string i.e. 'New', 'York, --> 'New York'
    if len(element) == 7:
        element[1] = element[0] + ' ' + element[1]
        del element[0]        
    elif len(element) == 17:
        element[1] = element[0] + ' ' + element[1]
        del element[0] 
    
    # make 'District', 'of', 'Columbia' into 'District of Columbia'
    elif len(element) == 8:
        element[2] = element[0] + ' ' + element[1] + ' ' + element[2]
        del element[0]
        del element[0] 
    elif len(element) == 18:
        element[2] = element[0] + ' ' + element[1] + ' ' + element[2]
        del element[0]
        del element[0]

    splitList.append(element)

# remove commas and unwanted columns
minList = []
for element in splitList:
    if len(element) == 6:
        element[1] = element[1].replace(',','')
        element = element[0:2]
        minList.append(element)
    else:
        element[1] = element[1] + ' ' + element[6] + ' ' + element[11]
        element = element[0:2]
        element[1] = element[1].split()
        element.insert(1, element[1][0])
        element.insert(2, element[2][1])
        element[3] = element[3][2] 
        element[1] = element[1].replace(',','')
        element[2] = element[2].replace(',','')
        element[3] = element[3].replace(',','')
        minList.append(element)
        
# group by census year
list1990 = []
list1980 = []
list1970 = []
list1960 = []
list1950 = []
list1940 = []
list1930 = []
list1920 = []
list1910 = []
list1900 = []
for index, element in enumerate(minList):
    if index < 51:
        list1990.append(((int(minList[index][1])),minList[index][0]))
        list1980.append(((int(minList[index][2])),minList[index][0]))
        list1970.append(((int(minList[index][3])),minList[index][0]))
    elif index >= 51 and index < 102:
        list1960.append(((int(minList[index][1])),minList[index][0]))
        list1950.append(((int(minList[index][2])),minList[index][0]))
        list1940.append(((int(minList[index][3])),minList[index][0])) 
    elif index >= 102 and index < 153:
        list1930.append(((int(minList[index][1])),minList[index][0]))
        list1920.append(((int(minList[index][2])),minList[index][0]))
        list1910.append(((int(minList[index][3])),minList[index][0]))
    elif index >=153:
        list1900.append(((int(minList[index][1])),minList[index][0]))

inputYear = input("Enter census year between 1900 to 1990: ")

if inputYear == '1900':
    print('Minimum: {0}\nMaximum: {1}'.format(min(list1900), max(list1900)))
elif inputYear == '1910':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1910), max(list1910)))
elif inputYear == '1920':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1920), max(list1920)))
elif inputYear == '1930':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1930), max(list1930)))
elif inputYear == '1940':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1940), max(list1940)))
elif inputYear == '1950':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1950), max(list1950)))
elif inputYear == '1960':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1960), max(list1960)))
elif inputYear == '1970':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1970), max(list1970)))
elif inputYear == '1980':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1980), max(list1980)))
elif inputYear == '1990':
     print('Minimum: {0}\nMaximum: {1}'.format(min(list1990), max(list1990)))
else:
    print('Year entered was not valid. Only enter census years from 1900 to 1990. Try again.')


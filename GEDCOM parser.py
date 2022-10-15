from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

file1 = open("output_file.txt","w")

# Path to your `.ged` file
file_path = 'C:\\Users\\rahul\\OneDrive\\Desktop\\cs 555\\gedcom parser\\Family GEDCOM.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

get_element_list = gedcom_parser.get_element_list()

tag_list = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE' ]

# Iterate through all elements
for element in get_element_list:
    str_element = str(element)
    falg = -1
    for a in tag_list:
        flag = str_element.find(a)
        if flag != -1:
            break 
    if flag != -1:
        temp = str_element.split()
        temp.insert(2,'Y')
    else:
        temp = str_element.split()
        temp.insert(2,'N')    
    a = temp[0] + '|' +temp[1] + '|'+temp[2] + '|'
    b = ' '.join(temp[3:])
    file1.write('\n'+'<--'+str_element)
    file1.write('-->'+a+b)
import re

m = re.match(r'You', 'Young Army')
print(m)
print(m.span())

m = re.match(r'ac*b', 'acbfdsda')
print(m)

pattern1 = r'Wally' #" "랑 ' '가 차이가 발생한다.

list1 = ['Wenda' , 'Wizard Whitebeard', 'Wally', 'Woof', 'Odlaw', 'The Wally Watchers']

m = ','.join(list1)
print(m)

m2 = re.search(pattern1, m)
print(m2.span())


import re

wally=r'Wally'
name_lst=['Wenda','Wizard Whitebeard','Wally','Woof','Odlaw','The Wally Watchers']

in_a_park=','.join(name_lst)
print(in_a_park)


wally_pos=re.search(wally,in_a_park)
print('Wally is there, It is in a range of',wally_pos.span())


wally_lst=re.findall(wally,in_a_park)
print('There are',len(wally_lst),'Wally.')

###############################################################3
import re

wally=r'Wally'
name_lst=['Wenda','Wizard Whitebeard','Wally','Woof','Odlaw','The Wally Watchers']

in_a_park=','.join(name_lst)
print(in_a_park)

waldo=r'Waldo'
walk_in_a_park=re.sub(wally, waldo, in_a_park)
print(walk_in_a_park)

waldo_candidate=re.finditer(waldo, walk_in_a_park)
for discovery in waldo_candidate:
	print('Waldo is there,It is in a range of', discovery.span())

    ##############################

import sys

scripts=sys.argv[0]
params=sys.argv[1:]

sourcefile=params[0]
targetfile=params[1]

def filecopy1(sourcefile,targetfile):
	with open(sourcefile) as fin:
		with open(targetfile, 'w+')  as fout:
			line=fin.readline()
			while line:
				fout.write(line)
				line=fin.readline()


print('source file [',sourcefile, ']')
print('target file [',targetfile, ']')

filecopy1(sourcefile,targetfile)
print('DONE')

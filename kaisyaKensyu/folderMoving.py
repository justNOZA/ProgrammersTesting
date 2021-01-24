import os,glob,shutil,sys

targets='working_dir'
if os.path.exists(targets):
	os.chdir(targets)
else:
	sys.exit('BYE')


suffixes=['txt','log','py','*']
directories=['textfiles','logs','scripts','others']

for directory in directories:
	os.mkdir(directory)
	print('create a directory')

for i,suffix in enumerate(suffixes):
	files=glob.glob('*.' + suffix)
	for file in files:
		shutil.move(file,directories[i])
		print('moving a file [ ', file, "] to ", directories[i])

print("Done")

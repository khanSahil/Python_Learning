
import shutil
import os
import re

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
grand_parent_dir = os.path.dirname(parent_dir)

file_directory = grand_parent_dir + "/PythonLearning/Complete-Python-3-Bootcamp/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/"
file = file_directory + "unzip_me_for_instructions.zip"
shutil.unpack_archive(file,current_dir + "/instruction_manual", 'zip')

results = []
pattern = r'\d{3}-\d{3}-\d{4}'

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

for folder , sub_folders , files in os.walk(os.getcwd()+"/instruction_manual"):
    for f in files:
        full_path = folder+'/'+f
        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())
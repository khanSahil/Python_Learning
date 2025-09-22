f = open('file1.txt', 'w+')
f.write("ONE_FILE")
f.close()

f = open('file2.txt', 'w+')
f.write("TWO_FILE")
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('file1.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')

import shutil
dir_to_zip = "/home/sahkhan/Python_Learning/python_zip_unzip/extracted_content"
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive('example.zip','extracted_archive', 'zip')

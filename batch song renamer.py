import glob
import re
import os

files = glob.iglob(input('Enter root directory: ') + '/**/*.mp3', recursive=True)
print(files, end='\n\n')
input('%i files. Enter to continue ...' % (len(files)))
for file in files:
    abs_filepath = os.path.join(os.path.dirname(__file__), file)
    containing_folder_path_abs = '\\'.join(abs_filepath.split('\\')[0:-1])

    [author, name_and_subs] = os.path.basename(abs_filepath).split(' - ', 2)
    parts = re.split("\s(?=feat)|\s(?=ft)|\s(?=\()|\s(?=\&)", name_and_subs, 1)
    if len(parts) == 1:
        new_filename = parts[0][0:-4] + ' - ' + author + '.mp3'
    else:
        new_filename = parts[0] + ' - ' + author + ' ' + parts[1]

    os.rename(abs_filepath, containing_folder_path_abs+'\\'+new_filename)

response = input('... done. Enter to exit...')

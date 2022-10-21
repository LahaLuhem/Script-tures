import glob
import re
import os
import platform

posix_separator = '\\' if platform.uname()[0] == 'Windows' else '/'

files = [file for file in glob.iglob(input('Enter root directory:\n') + '/**/*.mp3', recursive=True)]
print("\n________________________________________________________________\n\n"+("\n".join(list(map(lambda file: os.path.basename(file), files)))), end='\n')
print("\n________________________________________________________________\n")
input('%i files detected. Enter to continue ...' % (len(files)))
for file in files:
    containing_folder_path_abs = posix_separator.join(file.split(posix_separator)[0:-1])

    [author, name_and_subs] = os.path.basename(file).split(' - ', 2)
    parts = re.split("\s(?=feat)|\s(?=ft)|\s(?=\()|\s(?=\&)", name_and_subs, 1)
    if len(parts) == 1:
        new_filename = parts[0][0:-4] + ' - ' + author + '.mp3'
    else:
        new_filename = parts[0] + ' - ' + author + ' ' + parts[1]

    os.rename(file, containing_folder_path_abs+posix_separator+new_filename)

print("\n________________________________________________________________\n")

response = input('... done. Enter to exit...')

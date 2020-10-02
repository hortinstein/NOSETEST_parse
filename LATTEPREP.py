import os
import sys
import fileinput
import shutil, errno



def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise


old_dir = sys.argv[1]

#creates a new copy of the data
walk_dir = "student_"+old_dir
copyanything(old_dir,walk_dir)

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    
    for subdir in subdirs:
        print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)

        if ("__pycache__" in file_path):
            continue
        print('\t- file %s (full path: %s)' % (filename, file_path))
        for line in fileinput.input(file_path, inplace=True):
            print('{} {}'.format(fileinput.filelineno(), line), end='') # for Python 3

        # with open(file_path, 'rwb') as f:
        #     f_content = f.read()
        #     print(fullpath)

            #list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
            #list_file.write(f_content)
            #list_file.write(b'\n')
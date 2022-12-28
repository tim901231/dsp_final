import os

dir = "./mix/"
out_dir = "./out/"
for filename in os.listdir(dir):
    command = f'matlab -nodisplay -r "classical({dir + filename}, {out_dir + filename});exit"'
    os.system(command);
    
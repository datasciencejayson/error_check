
import os
import pathlib

source = "/data2/bsro/00028_ld_mvp1/programs/logs/headcount"

# get a full list of all logs in directory and find the newest one

file_list = [file for file in os.listdir(source) if '.log' in file]
temp_mtime = 0
for i, ivalue in enumerate(file_list):
    if '.log' in ivalue:
        temp_file = ivalue
        mtime = pathlib.Path(f"{source}/{ivalue}").stat().st_mtime
        if mtime > temp_mtime:
            temp_time = mtime
            final_file = temp_file
    print(final_file, 'is the newest log file')


# read in the log and remove the false positive "ERROR" terms

with open(f"{source}/{final_file}", 'r') as f:
    data = f.read()

data_check = data.replace('set ERROR', 'xx1').replace('if _ERROR_', 'xx2').replace('set the ERROR', 'xx3')
print(data_check)

# write a log file letting the user know if there is an error or not
error_list = ['Subject: Endeavor Error Log']

with open(f"{source}/error_check_{final_file}",'w') as f:
    if 'ERROR' in data_check:
        print('error')
        f.write(f'errors detected. Please address errors found in {final_file}')
        error_list.append(f'-errors found in {ivalue}')
    else:
        f.write(f'no errors detected.')
        error_list.append(f'-no errors found in {ivalue}')

with open(f"{source}/endeavor_error_email.txt",'w') as f:
    f.write(error_list[0] + "\r\n" + "\r\n" + error_list[1])


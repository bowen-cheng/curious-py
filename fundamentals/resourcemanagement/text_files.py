# File mode: wt means Writing Text file, this will create/overwrite a text file by given name
# Both mode nad encoding are optional but recommended to explicit
new_file = open('new_file.txt', mode='wt', encoding='utf-8')

# Write some texts
new_file.write('Output lines without new line. ')
# There is no "writeln" function, we need to append new lines ourselves
new_file.write('Output lines with new line\n')
# The new line symbol is universal in Python
# But the translation of new lines depends on the system where it runs
new_file.write('Last line of the file\n')

# close the file once we are done writing to it
new_file.close()

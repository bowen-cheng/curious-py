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
# Calling close() is required to actually write the data
new_file.close()

# Mode: Append Text
append_file = open('sample.txt', mode='at', encoding='utf-8')
# Use writelines to append an iterable series of strings at the end of the file
append_file.writelines([
    "First line appended\n",
    "Second line, ",
    "Still second line"
])
append_file.close()

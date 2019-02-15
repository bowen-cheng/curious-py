# This file is the entrance of this runnable directory
# This package can now be run as "python3 beyondbasics/packages/executable"
# If this dir is zipped into one file e.g. executable.zip, it can still run as "python3 executable.zip"

from run import Runner

print("This dir is executed")

r = Runner()
r.print()

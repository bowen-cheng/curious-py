"""
This __init__.py file tells Python the current directory is a "package"
launch Python console in beyondbasics dir and import readerpkg, the next line will be executed
"""
print('Reader package is imported, oh yeah!')

"""
The import statement makes the ReaderClass accessible at the package level

>>> import readerpkg
Reader package is imported
>>> r = readerpkg.ReaderClass('...')
>>> r.read()

or

>>> from readerpkg import ReaderClass
Reader package is imported
>>> r = ReaderClass("...")
>>> r.read()
"""
from readerpkg.reader_module import ReaderClass

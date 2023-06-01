"""if I need to import a python file, I simply write import that..., but if it is a package, and it is not in the same
directory as the same I am in, I need to specify from where and I write from (package) import python file """
# also I can say from python File, import (def function or class) and that is how to take it

from ErrorsAndExceptions import ErrorsAndExceptionsNotes
from ErrorsAndExceptions.ErrorsAndExceptionsNotes import raiseError

# and that is how we take file from a python file inside a package!!! package.file

# that makes the file, a module!!
# package is a collection of modules
#  if we delete the __init__ as we start the package, the package is not considered a package, making it a random directory

#  the default name of each module is main and if we type __name__ in print it will be __main__

# so we can say like this if __name__ -- '__main__: do this...  !!!!!!




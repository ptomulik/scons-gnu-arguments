"""`SConsGnuArguments`

This package provides definition of some commonly used SCons *arguments*
(concept impemented in `SConsArguments` package) when working on GNU-like
projects. The package contains several submodules, which provide more and
more predefined *arguments*

    - `SConsGnuArguments.InstallDirs` - GNU directory variables, i.e.
      ``$prefix``, ``$exec_prefix`` and such.

Each module provides at least two functions:

    - ``ArgumentNames()``, to list names of SCons *arguments* being provided by module,
    - ``ArgumentDeclarations()``, to retrieve actual *argument* declarations.

The typical usage pattern is (taking `InstallDirs` as example):

.. python::

    # SConstruct
    # ...
    decls = SConsArguments.ArgumentDeclarations() # somewhere
    # ...
    decls.update(SConsGnuArguments.InstallDirs.ArgumentDeclarations())
    # ...
"""

#
# Copyright (c) 2015 by Pawel Tomulik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

__docformat__ = "restructuredText"


## TODO: Place your code here

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

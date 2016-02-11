"""`SConsGnuArguments.AltPrograms`

SCons *arguments* for `Alternative Programs`_.

**General Description**

This module provides standard `autoconf output variables`_  which define paths
to `Alternative Programs`_. Each variable may be accessed via:

    - SCons environment, as construction variables (``env.subst('$variable')``),
    - SCons command line variables (``scons variable=value``),

Supported variables:
====================

    AWK
        The awk program
    EGREP
        The egrep program
    FGREP
        The fgrep program
    GREP
        The grep program
    INSTALL
        The program used to install files
    INSTALL_DATA
        The program used to install data
    INSTALL_PROGRAM
        The program used to install programs
    INSTALL_SCRIPT
        The program used to install scripts
    LEX
        The lex program
    LEX_OUTPUT_ROOT
        The base of the file name that the LEX generates
    LEXLIB
        Library that should be linked to LEX-generated program
    LN_S
        Either 'ln -s', 'cp -pR' or just 'ln'
    MKDIR_P
        Either 'mkdir -p' or 'install-sh'
    RANLIB
        The ranlib program
    SED
        The sed program
    YACC
        The yacc program

.. _autoconf output variables: http://www.gnu.org/software/autoconf/manual/autoconf.html#Output-Variable-Index
.. _Alternative Programs: http://www.gnu.org/software/autoconf/manual/autoconf.html#Alternative-Programs
"""


#
# Copyright (c) 2012-2015 by Pawel Tomulik
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

__docformat__ = 'restructuredText'

import SConsArguments
import SConsGnuArguments.Util

UNDEFINED = SConsArguments.UNDEFINED

#############################################################################
_std_arg_triples = [
    ( 'AWK',
      "The awk program",
      UNDEFINED ),
    ( 'EGREP',
      "The egrep program",
      UNDEFINED ),
    ( 'FGREP',
      "The fgrep program",
      UNDEFINED ),
    ( 'GREP',
      "The grep program",
      UNDEFINED ),
    ( 'INSTALL',
      "The program used to install files",
      UNDEFINED ),
    ( 'INSTALL_DATA',
       "The program used to install data",
      '${INSTALL}'),
    ( 'INSTALL_PROGRAM',
      "The program used to install programs",
      '${INSTALL}'),
    ( 'INSTALL_SCRIPT',
      "The program used to install scripts",
      '${INSTALL}'),
    ( 'LEX',
      "The lex program",
      UNDEFINED ),
    ( 'LEX_OUTPUT_ROOT',
      "The base of the file name that the LEX generates",
      UNDEFINED ),
    ( 'LEXLIB',
      "Library that should be linked to LEX-generated programs",
      UNDEFINED ),
    ( 'LN_S',
      "Either 'ln -s', 'cp -pR' or just 'ln'",
      UNDEFINED ),
    ( 'MKDIR_P',
      "Either 'mkdir -p' or 'install-sh'",
      UNDEFINED ),
    ( 'RANLIB',
      "The ranlib program",
      UNDEFINED ),
    ( 'SED',
      "The sed program",
      UNDEFINED ),
    ( 'YACC',
      "The yacc program",
      UNDEFINED ),
]
"""Predefined arguments. This is for internal use, it IS **NOT a part of public API**"""

#############################################################################
def __init_module_vars():
    # nothing here yet,
    pass
__init_module_vars()

#############################################################################
def Names(name_filter = lambda x : True):
    """Return list of argument names for alternative programs.

    :Parameters:
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
    :Returns:
        the list of standard GNU directory variable names
    """
    return SConsGnuArguments.Util.names_from_triples(_std_arg_triples, name_filter)

###############################################################################
def Declarations(**kw):
    """Return declarations of *arguments* related to alternative programs.

    :Keywords:
        defaults : dict
            user-specified default values for the *arguments* being declared,
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
        nameconv : `SConsArguments._ArgumentNameConv`
            a `SConsArguments._ArgumentNameConv` object used to transform
            *argument* names to *endpoint* (construction variable, command-line
            variable, command-line option) names,
        env_key_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        env_key_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        env_key_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        var_key_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        var_key_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        var_key_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_key_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_key_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_key_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`, note that
            `Declarations` sets this to ``False`` by default,
        opt_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_name_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_name_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        option_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`.

    :Returns:
        an instance of `SConsArguments._ArgumentDeclarations`
    """
    if not 'opt_key_transform' in kw:
        kw['opt_key_transform'] = False
    return SConsGnuArguments.Util.arguments_from_triples(_std_arg_triples, **kw)

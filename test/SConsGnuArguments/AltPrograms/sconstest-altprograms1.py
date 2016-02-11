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

__docformat__ = "restructuredText"

"""
Tests SConsGnuArguments.AltPrograms.Declarations() with no arguments, verify
the help strings it generates
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture('../../../SConsGnuArguments', 'site_scons/SConsGnuArguments')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsGnuArguments.AltPrograms

env = Environment(tools = [])
var = Variables()
decls = SConsGnuArguments.AltPrograms.Declarations()
args = decls.Commit(env, var, True)

AddOption('--help-variables', dest='help_variables', action='store_true',
          help='print help for CLI variables')
if GetOption('help_variables'):
    print args.GenerateVariablesHelpText(var, env)
""")

test.run('-Q --help-variables')

lines = [
r"""EGREP: The egrep program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""INSTALL_DATA: The program used to install data""",
r"""    default: ${INSTALL}""",
r"""    actual: """,

r"""RANLIB: The ranlib program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""YACC: The yacc program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""FGREP: The fgrep program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""INSTALL: The program used to install files""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""MKDIR_P: Either 'mkdir -p' or 'install-sh'""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""INSTALL_PROGRAM: The program used to install programs""",
r"""    default: ${INSTALL}""",
r"""    actual: """,

r"""INSTALL_SCRIPT: The program used to install scripts""",
r"""    default: ${INSTALL}""",
r"""    actual: """,

r"""GREP: The grep program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SED: The sed program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""AWK: The awk program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""LEX: The lex program""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""LN_S: Either 'ln -s', 'cp -pR' or just 'ln'""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""LEX_OUTPUT_ROOT: The base of the file name that the LEX generates""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""LEXLIB: Library that should be linked to LEX-generated programs""",
r"""    default: UNDEFINED""",
r"""    actual: None""",
]

test.must_contain_all_lines(test.stdout(), lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

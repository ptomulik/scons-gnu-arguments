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
Tests SConsGnuArguments.AltPrograms.Declarations(), test whether they enter
scons environment
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture('../../../SConsGnuArguments', 'site_scons/SConsGnuArguments')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsGnuArguments.AltPrograms

env = Environment(tools=[])
env.Replace(install_package = 'my_install_package', package = 'my_package')
var = Variables()
decls = SConsGnuArguments.AltPrograms.Declarations()
args = decls.Commit(env, var, True)
args.Postprocess(env, var, True)

proxy = args.EnvProxy(env)
for k in SConsGnuArguments.AltPrograms.Names():
    print proxy.subst("%s : ${%s}" % (k, k))
""")

test_tab = [
  (
    ['AWK=/my/awk', 'INSTALL=/my/install'],
    [
        r"""AWK : /my/awk""",
        r"""EGREP :""",
        r"""FGREP :""",
        r"""GREP :""",
        r"""INSTALL : /my/install""",
        r"""INSTALL_DATA : /my/install""",
        r"""INSTALL_PROGRAM : /my/install""",
        r"""INSTALL_SCRIPT : /my/install""",
        r"""LEX :""",
        r"""LEX_OUTPUT_ROOT :""",
        r"""LEXLIB :""",
        r"""LN_S :""",
        r"""MKDIR_P :""",
        r"""RANLIB :""",
        r"""SED :""",
        r"""YACC :""",
    ]
  ),
]

for cli_vars, chk_lines in test_tab:
    test.run(['-Q'] + cli_vars)
    test.must_contain_all_lines(test.stdout(), chk_lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

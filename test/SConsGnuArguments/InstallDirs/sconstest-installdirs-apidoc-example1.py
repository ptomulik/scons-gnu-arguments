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
Tests SConsGnuArguments.InstallDirs - example 1 in API docs.
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture('../../../SConsGnuArguments', 'site_scons/SConsGnuArguments')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsGnuArguments.InstallDirs

env = Environment()
env.Replace(install_package = 'my_install_package', package = 'my_package')
var = Variables()
decls = SConsGnuArguments.InstallDirs.ArgumentDecls()
args = decls.Commit(env, var, True)
args.Postprocess(env, var, True)

print env.subst("prefix : ${prefix}")
print env.subst("bindir : ${bindir}")
""")

test.run(['-Q'])
test.must_contain_all_lines(test.stdout(), ["""prefix : /usr/local""", """bindir : /usr/local/bin"""])

test.run(['-Q', 'prefix=/usr'])
test.must_contain_all_lines(test.stdout(), ["""prefix : /usr""", """bindir : /usr/bin"""])

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

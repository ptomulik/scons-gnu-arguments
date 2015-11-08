""" SConsGnuArguments.AltProgramsTests

Unit tests for SConsGnuArguments.AltPrograms
"""

__docformat__ = "restructuredText"

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

import SConsGnuArguments.AltPrograms
import SConsArguments
import unittest

# The mock module does not come as a part of python 2.x stdlib, it has to be
# installed separatelly. Here we detect whether mock is present and if not,
# we skip all the tests that use mock.
_mock_missing = True
try:
    # Try unittest.mock first (python 3.x) ...
    import unittest.mock as mock
    _mock_missing = False
except ImportError:
    try:
        # ... then try mock (python 2.x)
        import mock
        _mock_missing = False
    except ImportError:
        # mock not installed
        pass

UNDEFINED = SConsArguments.UNDEFINED

_test_arg_triples = [
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

_test_arg_names = [
    'AWK',
    'EGREP',
    'FGREP',
    'GREP',
    'INSTALL',
    'INSTALL_DATA',
    'INSTALL_PROGRAM',
    'INSTALL_SCRIPT',
    'LEX',
    'LEX_OUTPUT_ROOT',
    'LEXLIB',
    'LN_S',
    'MKDIR_P',
    'RANLIB',
    'SED',
    'YACC',
]

#############################################################################
def __init_module_vars(**kw):
    pass
__init_module_vars()

#############################################################################
class Test__std_arg_triples(unittest.TestCase):
    """Test _std_arg_triples"""
    @staticmethod
    def find_triple(triples, name):
        for triple in triples:
            if triple[0] == name:
                return triple
        return None

    def chck_triple(self,name):
        t1 = Test__std_arg_triples.find_triple(SConsGnuArguments.AltPrograms._std_arg_triples, name)
        t2 = Test__std_arg_triples.find_triple(_test_arg_triples, name)
        self.assertTrue(t1, "triple '%s' not found in AltPrograms._std_arg_triples" % name)
        self.assertTrue(t2, "triple '%s' not found in AltProgramsTests._test_arg_triples" % name)
        self.assertEqual(t1[0], t2[0]) # name
        self.assertEqual(t1[1], t2[1]) # help message
        self.assertEqual(t1[2], t2[2]) # default value
        
    def test_AWK(self):
        """Test 'AWK' in AltPrograms._std_arg_triples"""
        self.chck_triple('AWK')
        
    def test_EGREP(self):
        """Test 'EGREP' in AltPrograms._std_arg_triples"""
        self.chck_triple('EGREP')
        
    def test_FGREP(self):
        """Test 'FGREP' in AltPrograms._std_arg_triples"""
        self.chck_triple('FGREP')
        
    def test_GREP(self):
        """Test 'GREP' in AltPrograms._std_arg_triples"""
        self.chck_triple('GREP')

    def test_INSTALL(self):
        """Test 'INSTALL' in AltPrograms._std_arg_triples"""
        self.chck_triple('INSTALL')
        
    def test_INSTALL_DATA(self):
        """Test 'INSTALL_DATA' in AltPrograms._std_arg_triples"""
        self.chck_triple('INSTALL_DATA')
        
    def test_INSTALL_PROGRAM(self):
        """Test 'INSTALL_PROGRAM' in AltPrograms._std_arg_triples"""
        self.chck_triple('INSTALL_PROGRAM')
        
    def test_INSTALL_SCRIPT(self):
        """Test 'INSTALL_SCRIPT' in AltPrograms._std_arg_triples"""
        self.chck_triple('INSTALL_SCRIPT')
        
    def test_LEX(self):
        """Test 'LEX' in AltPrograms._std_arg_triples"""
        self.chck_triple('LEX')
        
    def test_LEX_OUTPUT_ROOT(self):
        """Test 'LEX_OUTPUT_ROOT' in AltPrograms._std_arg_triples"""
        self.chck_triple('LEX_OUTPUT_ROOT')
        
    def test_LEXLIB(self):
        """Test 'LEXLIB' in AltPrograms._std_arg_triples"""
        self.chck_triple('LEXLIB')
        
    def test_LN_S(self):
        """Test 'LN_S' in AltPrograms._std_arg_triples"""
        self.chck_triple('LN_S')
        
    def test_MKDIR_P(self):
        """Test 'MKDIR_P' in AltPrograms._std_arg_triples"""
        self.chck_triple('MKDIR_P')
        
    def test_RANLIB(self):
        """Test 'RANLIB' in AltPrograms._std_arg_triples"""
        self.chck_triple('RANLIB')
        
    def test_SED(self):
        """Test 'SED' in AltPrograms._std_arg_triples"""
        self.chck_triple('SED')
        
    def test_YACC(self):
        """Test 'YACC' in AltPrograms._std_arg_triples"""
        self.chck_triple('YACC')

class Test_Names(unittest.TestCase):
    def test_Names_1(self):
        """AltPrograms.Names() should return all argument names"""
        names = SConsGnuArguments.AltPrograms.Names()
        self.assertListEqual(names, _test_arg_names)
    def test_Names_2(self):
        """AltPrograms.Names(lambda s : s == 'AWK') should return ['AWK']"""
        names = SConsGnuArguments.AltPrograms.Names(lambda s : s == 'AWK')
        self.assertListEqual(names, ['AWK'])
    def test_Names_3(self):
        """AltPrograms.Names(['AWK','FOO']) should return ['AWK']"""
        names = SConsGnuArguments.AltPrograms.Names(['AWK','FOO'])
        self.assertListEqual(names, ['AWK'])
    def test_Names_4(self):
        """AltPrograms.Names(lambda s : s == 'inexistent') should return []"""
        names = SConsGnuArguments.AltPrograms.Names(lambda s : s == 'inexistent')
        self.assertListEqual(names, [])

class Test_Declarations(unittest.TestCase):
    def test_Declarations_1(self):
        """AltPrograms.Declarations() should return all argument declaratins"""
        decls = SConsGnuArguments.AltPrograms.Declarations()
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertEqual(decls[key].get_env_key(), key)
            self.assertEqual(decls[key].get_var_key(), key)
            self.assertFalse(decls[key].has_opt_decl())
            self.assertEqual(decls[key].get_env_default(), default)
            self.assertEqual(decls[key].get_var_default(), default)

    def test_Declarations_2(self):
        """AltPrograms.Declarations(env_key_transform=False) should not create construction variables"""
        decls = SConsGnuArguments.AltPrograms.Declarations(env_key_transform = False)
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertFalse(decls[key].has_env_decl())
            self.assertTrue(decls[key].has_var_decl())
            self.assertFalse(decls[key].has_opt_decl())

    def test_Declarations_3(self):
        """AltPrograms.Declarations(var_key_transform=False) should not create command-line variables"""
        decls = SConsGnuArguments.AltPrograms.Declarations(var_key_transform = False)
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertTrue(decls[key].has_env_decl())
            self.assertFalse(decls[key].has_var_decl())
            self.assertFalse(decls[key].has_opt_decl())

    def test_Declarations_4(self):
        """AltPrograms.Declarations(opt_key_transform=True) should create command-line options"""
        decls = SConsGnuArguments.AltPrograms.Declarations(opt_key_transform = True)
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertTrue(decls[key].has_env_decl())
            self.assertTrue(decls[key].has_var_decl())
            self.assertTrue(decls[key].has_opt_decl())

    def test_Declarations_5(self):
        """AltPrograms.Declarations(name_filter = lambda s : s == 'AWK') should only create 'AWK' argument"""
        decls = SConsGnuArguments.AltPrograms.Declarations(name_filter = lambda s : s == 'AWK')
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        self.assertEqual(len(decls), 1)
        self.assertEqual(decls['AWK'].get_env_key(), 'AWK')
        self.assertEqual(decls['AWK'].get_var_key(), 'AWK')
        self.assertFalse(decls['AWK'].has_opt_decl())

    def test_Declarations_6(self):
        """AltPrograms.Declarations(name_filter = ['AWK', 'FOO']) should only create 'AWK' argument"""
        decls = SConsGnuArguments.AltPrograms.Declarations(name_filter = ['AWK', 'FOO'])
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        self.assertEqual(len(decls), 1)
        self.assertEqual(decls['AWK'].get_env_key(), 'AWK')
        self.assertEqual(decls['AWK'].get_var_key(), 'AWK')
        self.assertFalse(decls['AWK'].has_opt_decl())

    def test_Declarations_7(self):
        """Test AltPrograms.Declarations() with prefixes/suffixes"""
        decls = SConsGnuArguments.AltPrograms.Declarations(
                    env_key_prefix = 'ENV_', env_key_suffix = '_VNE',
                    var_key_prefix = 'VAR_', var_key_suffix = '_RAV',
                    opt_key_prefix = 'opt_', opt_key_suffix = '_pto',
                    opt_name_prefix = 'on_', opt_name_suffix = '_no',
                    opt_prefix = '-', opt_key_transform=True
                )
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertEqual(decls[key].get_env_key(), 'ENV_' + key + '_VNE')
            self.assertEqual(decls[key].get_var_key(), 'VAR_' + key + '_RAV')
            self.assertEqual(decls[key].get_opt_key(), 'opt_' + key.lower() + '_pto')
            self.assertEqual(decls[key].get_opt_decl()[0], ('-on-' + key.lower().replace('_','-') + '-no',))

#############################################################################
if __name__ == "__main__":
    ldr = unittest.TestLoader()
    suite = unittest.TestSuite()
    # Load tests to test suite
    tclasses = [ Test__std_arg_triples
               , Test_Names
               , Test_Declarations
               ]

    for tclass in tclasses:
        suite.addTests(ldr.loadTestsFromTestCase(tclass))

    if not unittest.TextTestRunner(verbosity = 2).run(suite).wasSuccessful():
        sys.exit(1)

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

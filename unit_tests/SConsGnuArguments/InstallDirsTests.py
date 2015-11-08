""" SConsGnuArguments.InstallDirsTests

Unit tests for SConsGnuArguments.InstallDirs
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

import SConsGnuArguments.InstallDirs
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

_test_arg_triples = [
  ( 'prefix',
    'Installation prefix',
    '/usr/local' ),
  ( 'exec_prefix',
    'Installation prefix for executable files',
    '${prefix}' ),
  ( 'bindir',
    'The directory for installing executable programs that users can run.',
    '${exec_prefix}/bin' ),
  ( 'sbindir',
    'The directory for installing executable programs that can be run from the'
  + ' shell, but are only generally useful to system administrators.',
    '${exec_prefix}/sbin' ),
  ( 'libexecdir',
    'The directory for installing executable programs to be run by other'
  + ' programs rather than by users.',
    '${exec_prefix}/libexec' ),
  ( 'datarootdir',
    'The root of the directory tree for read-only architecture-independent'
  + ' data files.',
    '${prefix}/share' ),
  ( 'datadir',
    'The directory for installing idiosyncratic read-only'
  + ' architecture-independent data files for this program.',
    '${datarootdir}' ),
  ( 'sysconfdir',
    'The directory for installing read-only data files that pertain to a single'
  + ' machine - that is to say, files for configuring a host.',
    '${prefix}/etc' ),
  ( 'sharedstatedir',
    'The directory for installing architecture-independent data files which'
  + ' the programs modify while they run.',
    '${prefix}/com' ),
  ( 'localstatedir',
    'The directory for installing data files which the programs modify while'
  + ' they run, and that pertain to one specific machine.',
    '${prefix}/var' ),
  ( 'includedir',
    'The directory for installing header files to be included by user programs'
  + ' with the C "#include" preprocessor directive.',
    '${prefix}/include' ),
  ( 'oldincludedir',
    'The directory for installing "#include" header files for use with compilers'
  + ' other than GCC.',
    '/usr/include' ),
  ( 'docdir',
    'The directory for installing documentation files (other than Info) for this'
  + ' package.',
    '${datarootdir}/doc/${install_package}' ),
  ( 'infodir',
    'The directory for installing the Info files for this package.',
    '${datarootdir}/info' ),
  ( 'htmldir',
    'Directory for installing documentation files in the html format.',
    '${docdir}' ),
  ( 'dvidir',
    'Directory for installing documentation files in the dvi format.',
    '${docdir}' ),
  ( 'pdfdir',
    'Directory for installing documentation files in the pdf format.',
    '${docdir}' ),
  ( 'psdir',
    'Directory for installing documentation files in the ps format.',
    '${docdir}' ),
  ( 'libdir',
    'The directory for object files and libraries of object code.',
    '${exec_prefix}/lib' ),
  ( 'lispdir',
    'The directory for installing any Emacs Lisp files in this package.',
    '${datarootdir}/emacs/site-lisp' ),
  ( 'localedir',
    'The directory for installing locale-specific message catalogs for this'
  + ' package.',
    '${datarootdir}/locale' ),
  ( 'mandir',
    'The top-level directory for installing the man pages (if any) for this'
  + ' package.',
    '${datarootdir}/man' ),
  ( 'pkgdatadir',
    'The directory for installing idiosyncratic read-only'
  + ' architecture-independent data files for this program.',
    '${datadir}/${package}' ),
  ( 'pkgincludedir',
    'The directory for installing header files to be included by user programs'
  + ' with the C "#include" preprocessor directive.',
    '${includedir}/${package}' ),
  ( 'pkglibdir',
    'The directory for object files and libraries of object code.',
    '${libdir}/${package}' ),
  ( 'pkglibexecdir',
    'The directory for installing executable programs to be run by other'
  + ' programs rather than by users.',
    '${libexecdir}/${package}' )
]

_test_arg_names = [
  'prefix',
  'exec_prefix',
  'bindir',
  'sbindir',
  'libexecdir',
  'datarootdir',
  'datadir',
  'sysconfdir',
  'sharedstatedir',
  'localstatedir',
  'includedir',
  'oldincludedir',
  'docdir',
  'infodir',
  'htmldir',
  'dvidir',
  'pdfdir',
  'psdir',
  'libdir',
  'lispdir',
  'localedir',
  'mandir',
  'pkgdatadir',
  'pkgincludedir',
  'pkglibdir',
  'pkglibexecdir'
]

#############################################################################
def __init_module_vars(**kw):
    man_sections = kw.get('man_sections', map(lambda x : str(x), range(1,10)) + ['n','l'])
    for sec in man_sections:
        dir_help = 'The directory for installing section %s man pages.' % sec
        ext_help = 'The file name extension for installed section %s man pages.' % sec
        _test_arg_triples.append( ('man%sdir' % sec, dir_help, '${mandir}/man%s' %sec) )
        _test_arg_triples.append( ('man%sext' % sec, ext_help, '.%s' %sec) )
        _test_arg_names.append('man%sdir' % sec)
        _test_arg_names.append('man%sext' % sec)
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
        t1 = Test__std_arg_triples.find_triple(SConsGnuArguments.InstallDirs._std_arg_triples, name)
        t2 = Test__std_arg_triples.find_triple(_test_arg_triples, name)
        self.assertTrue(t1, "triple '%s' not found in InstallDirs._std_arg_triples" % name)
        self.assertTrue(t2, "triple '%s' not found in InstallDirsTests._test_arg_triples" % name)
        self.assertEqual(t1[0], t2[0]) # name
        self.assertEqual(t1[1], t2[1]) # help message
        self.assertEqual(t1[2], t2[2]) # default value
        
    def test_prefix(self):
        """Test 'prefix' in InstallDirs._std_arg_triples"""
        self.chck_triple('prefix')
    def test_exec_prefix(self):
        """Test 'exec_prefix' in InstallDirs._std_arg_triples"""
        self.chck_triple('exec_prefix')
    def test_bindir(self):
        """Test 'bindir' in InstallDirs._std_arg_triples"""
        self.chck_triple('bindir')
    def test_sbindir(self):
        """Test 'sbindir' in InstallDirs._std_arg_triples"""
        self.chck_triple('sbindir')
    def test_libexecdir(self):
        """Test 'libexecdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('libexecdir')
    def test_datarootdir(self):
        """Test 'datarootdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('datarootdir')
    def test_datadir(self):
        """Test 'XXX' in InstallDirs._std_arg_triples"""
        self.chck_triple('datadir')
    def test_sysconfdir(self):
        """Test 'sysconfdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('sysconfdir')
    def test_sharedstatedir(self):
        """Test 'sharedstatedir' in InstallDirs._std_arg_triples"""
        self.chck_triple('sharedstatedir')
    def test_localstatedir(self):
        """Test 'localstatedir' in InstallDirs._std_arg_triples"""
        self.chck_triple('localstatedir')
    def test_includedir(self):
        """Test 'includedir' in InstallDirs._std_arg_triples"""
        self.chck_triple('includedir')
    def test_oldincludedir(self):
        """Test 'oldincludedir' in InstallDirs._std_arg_triples"""
        self.chck_triple('oldincludedir')
    def test_docdir(self):
        """Test 'docdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('docdir')
    def test_infodir(self):
        """Test 'infodir' in InstallDirs._std_arg_triples"""
        self.chck_triple('infodir')
    def test_htmldir(self):
        """Test 'htmldir' in InstallDirs._std_arg_triples"""
        self.chck_triple('htmldir')
    def test_dvidir(self):
        """Test 'dvidir' in InstallDirs._std_arg_triples"""
        self.chck_triple('dvidir')
    def test_pdfdir(self):
        """Test 'pdfdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('pdfdir')
    def test_psdir(self):
        """Test 'psdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('psdir')
    def test_libdir(self):
        """Test 'libdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('libdir')
    def test_lispdir(self):
        """Test 'lispdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('lispdir')
    def test_localedir(self):
        """Test 'localedir' in InstallDirs._std_arg_triples"""
        self.chck_triple('localedir')
    def test_mandir(self):
        """Test 'mandir' in InstallDirs._std_arg_triples"""
        self.chck_triple('mandir')
    def test_man1dir(self):
        """Test 'man1dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man1dir')
    def test_man2dir(self):
        """Test 'man2dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man2dir')
    def test_man3dir(self):
        """Test 'man3dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man3dir')
    def test_man4dir(self):
        """Test 'man4dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man4dir')
    def test_man5dir(self):
        """Test 'man5dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man5dir')
    def test_man6dir(self):
        """Test 'man6dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man6dir')
    def test_man7dir(self):
        """Test 'man7dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man7dir')
    def test_man8dir(self):
        """Test 'man8dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man8dir')
    def test_man9dir(self):
        """Test 'man9dir' in InstallDirs._std_arg_triples"""
        self.chck_triple('man9dir')
    def test_manndir(self):
        """Test 'manndir' in InstallDirs._std_arg_triples"""
        self.chck_triple('manndir')
    def test_manldir(self):
        """Test 'manldir' in InstallDirs._std_arg_triples"""
        self.chck_triple('manldir')
    def test_man1ext(self):
        """Test 'man1ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man1ext')
    def test_man2ext(self):
        """Test 'man2ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man2ext')
    def test_man3ext(self):
        """Test 'man3ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man3ext')
    def test_man4ext(self):
        """Test 'man4ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man4ext')
    def test_man5ext(self):
        """Test 'man5ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man5ext')
    def test_man6ext(self):
        """Test 'man6ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man6ext')
    def test_man7ext(self):
        """Test 'man7ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man7ext')
    def test_man8ext(self):
        """Test 'man8ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man8ext')
    def test_man9ext(self):
        """Test 'man9ext' in InstallDirs._std_arg_triples"""
        self.chck_triple('man9ext')
    def test_mannext(self):
        """Test 'mannext' in InstallDirs._std_arg_triples"""
        self.chck_triple('mannext')
    def test_manlext(self):
        """Test 'manlext' in InstallDirs._std_arg_triples"""
        self.chck_triple('manlext')
    def test_pkgdatadir(self):
        """Test 'pkgdatadir' in InstallDirs._std_arg_triples"""
        self.chck_triple('pkgdatadir')
    def test_pkgincludedir(self):
        """Test 'pkgincludedir' in InstallDirs._std_arg_triples"""
        self.chck_triple('pkgincludedir')
    def test_pkglibdir(self):
        """Test 'pkglibdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('pkglibdir')
    def test_pkglibexecdir(self):
        """Test 'pkglibexecdir' in InstallDirs._std_arg_triples"""
        self.chck_triple('pkglibexecdir')

class Test__map_std_arg_triples(unittest.TestCase):
    def test__map_std_arg_triples_1(self):
        """InstallDirs._map_std_arg_triples(lambda *x : x) should return InstallDirs._std_arg_triples"""
        triples = SConsGnuArguments.InstallDirs._map_std_arg_triples(lambda *x : x)
        self.assertListEqual(triples, SConsGnuArguments.InstallDirs._std_arg_triples)
    def test__map_std_arg_triples_2(self):
        """InstallDirs._map_std_arg_triples(lambda *x : x, lambda x : False) should return []"""
        triples = SConsGnuArguments.InstallDirs._map_std_arg_triples(lambda *x : x, lambda s : False)
        self.assertListEqual(triples, [])
    def test__map_std_arg_triples_3(self):
        """InstallDirs._map_std_arg_triples(lambda *x : (x[0],), lambda x : x=='prefix') should return [('prefix',)]"""
        triples = SConsGnuArguments.InstallDirs._map_std_arg_triples(lambda *x : (x[0],), lambda s : s == 'prefix')
        self.assertListEqual(triples, [('prefix',)])

class Test_ArgumentNames(unittest.TestCase):
    def test_ArgumentNames_1(self):
        """InstallDirs.ArgumentNames() should return all argument names"""
        names = SConsGnuArguments.InstallDirs.ArgumentNames()
        self.assertListEqual(names, _test_arg_names)
    def test_ArgumentNames_2(self):
        """InstallDirs.ArgumentNames(lambda s : s == 'prefix') should return ['prefix']"""
        names = SConsGnuArguments.InstallDirs.ArgumentNames(lambda s : s == 'prefix')
        self.assertListEqual(names, ['prefix'])
    def test_ArgumentNames_3(self):
        """InstallDirs.ArgumentNames(lambda s : s == 'inexistent') should return []"""
        names = SConsGnuArguments.InstallDirs.ArgumentNames(lambda s : s == 'inexistent')
        self.assertListEqual(names, [])

class Test_ArgumentDecls(unittest.TestCase):
    def test_ArgumentDecls_1(self):
        """InstallDirs.ArgumentDecls() should return all argument declaratins"""
        decls = SConsGnuArguments.InstallDirs.ArgumentDecls()
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertEqual(decls[key].get_env_key(), key)
            self.assertEqual(decls[key].get_var_key(), key)
            self.assertFalse(decls[key].has_opt_decl())
            self.assertEqual(decls[key].get_env_default(), default)
            self.assertEqual(decls[key].get_var_default(), default)

    def test_ArgumentDecls_2(self):
        """InstallDirs.ArgumentDecls(env_key_transform=False) should not create construction variables"""
        decls = SConsGnuArguments.InstallDirs.ArgumentDecls(env_key_transform = False)
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertFalse(decls[key].has_env_decl())
            self.assertTrue(decls[key].has_var_decl())
            self.assertFalse(decls[key].has_opt_decl())

    def test_ArgumentDecls_3(self):
        """InstallDirs.ArgumentDecls(var_key_transform=False) should not create command-line variables"""
        decls = SConsGnuArguments.InstallDirs.ArgumentDecls(var_key_transform = False)
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertTrue(decls[key].has_env_decl())
            self.assertFalse(decls[key].has_var_decl())
            self.assertFalse(decls[key].has_opt_decl())

    def test_ArgumentDecls_4(self):
        """InstallDirs.ArgumentDecls(opt_key_transform=True) should create command-line options"""
        decls = SConsGnuArguments.InstallDirs.ArgumentDecls(opt_key_transform = True)
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        for (key, hlp, default) in _test_arg_triples:
            self.assertEqual(type(decls[key]), SConsArguments._ArgumentDecl)
            self.assertTrue(decls[key].has_env_decl())
            self.assertTrue(decls[key].has_var_decl())
            self.assertTrue(decls[key].has_opt_decl())

    def test_ArgumentDecls_5(self):
        """InstallDirs.ArgumentDecls(name_filter = lambda s : s == 'prefix') should only create 'prefix' argument"""
        decls = SConsGnuArguments.InstallDirs.ArgumentDecls(name_filter = lambda s : s == 'prefix')
        self.assertEqual(type(decls), SConsArguments._ArgumentDecls)
        self.assertEqual(len(decls), 1)
        self.assertEqual(decls['prefix'].get_env_key(), 'prefix')
        self.assertEqual(decls['prefix'].get_var_key(), 'prefix')
        self.assertFalse(decls['prefix'].has_opt_decl())

    def test_ArgumentDecls_6(self):
        """Test InstallDirs.ArgumentDecls() with prefixes/suffixes"""
        decls = SConsGnuArguments.InstallDirs.ArgumentDecls(
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
               , Test__map_std_arg_triples
               , Test_ArgumentNames
               , Test_ArgumentDecls
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

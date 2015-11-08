"""`SConsGnuArguments.InstallDirs`

Provides `GNU directory variables`_ as SCons *arguments*.

**General Description**

This module provides standard `GNU directory variables`_ defined by `GNU
Coding Standards`_, for example ``$prefix``, ``$bindir`` or ``$sysconfdir``.
The variables defined here may be easilly added to:

    - SCons environment, as construction variables (``env.subst('$variable')``),
    - SCons command line variables (``scons variable=value``),
    - SCons command line options (``scons --variable=value``).

**Quick start**

.. python::
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

Running examples::

    ptomulik@barakus:$ scons -Q
    prefix : /usr/local
    bindir : /usr/local/bin

    ptomulik@barakus:$ scons -Q prefix=/usr
    prefix : /usr
    bindir : /usr/bin


**Supported variables**

  prefix
      Installation prefix
  exec_prefix
      Installation prefix for executable files
  bindir
      The directory for installing executable programs that users can run.
  sbindir
      The directory for installing executable programs that can be run from the
      shell, but are only generally useful to system administrators.
  libexecdir
      The directory for installing executable programs to be run by other
      programs rather than by users.
  datarootdir
      The root of the directory tree for read-only architecture-independent
      data files.
  datadir
      The directory for installing idiosyncratic read-only
      architecture-independent data files for this program.
  sysconfdir
      The directory for installing read-only data files that pertain to a single
      machine - that is to say, files for configuring a host.
  sharedstatedir
      The directory for installing architecture-independent data files which
      the programs modify while they run.
  localstatedir
      The directory for installing data files which the programs modify while
      they run, and that pertain to one specific machine.
  includedir
      The directory for installing header files to be included by user programs
      with the C ``#include`` preprocessor directive.
  oldincludedir
      The directory for installing ``#include`` header files for use with compilers
      other than GCC.
  docdir
      The directory for installing documentation files (other than Info) for this
      package.
  infodir
      The directory for installing the Info files for this package.
  htmldir
      Directory for installing documentation files in the html format.
  dvidir
      Directory for installing documentation files in the dvi format.
  pdfdir
      Directory for installing documentation files in the pdf format.
  psdir
      Directory for installing documentation files in the ps format.
  libdir
      The directory for object files and libraries of object code.
  lispdir
      The directory for installing any Emacs Lisp files in this package.
  localedir
      The directory for installing locale-specific message catalogs for this
      package.
  mandir
      The top-level directory for installing the man pages (if any) for this
      package.
  man1dir .. man9dir
      Simmilar to mandir
  man1ext .. man9ext
      Extensions for manpage files.
  pkgdatadir
      The directory for installing idiosyncratic read-only
      architecture-independent data files for this program.
  pkgincludedir
      The directory for installing header files to be included by user programs
      with the C ``#include`` preprocessor directive.
  pkglibdir
      The directory for object files and libraries of object code.
  pkglibexecdir
      The directory for installing executable programs to be run by other
      programs rather than by users.

.. _GNU directory variables: http://www.gnu.org/prep/standards/html_node/Directory-Variables.html
.. _GNU Coding Standards: http://www.gnu.org/prep/standards/html_node/
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

import os
import SConsArguments

#############################################################################
# NOTE: variable substitutions must be in curly brackets, so use ${prefix}
#       and not $prefix. This is required for proper prefixing/suffixing and
#       transforming in certain parts of library
_std_arg_triples = [
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
"""Standard list of arguments for GNU install directories. This is internal
attribute and IS **NOT a part of public API**"""

#############################################################################
def __init_module_vars(**kw):
    """Initializes some module-level variables. This is an internal function
    and IS **NOT a part of public API**."""
    man_sections = kw.get('man_sections', map(lambda x : str(x), range(1,10)) + ['n','l'])
    for sec in man_sections:
        dir_help = 'The directory for installing section %s man pages.' % sec
        ext_help = 'The file name extension for installed section %s man pages.' % sec
        _std_arg_triples.append( ('man%sdir' % sec, dir_help, '${mandir}/man%s' %sec) )
        _std_arg_triples.append( ('man%sext' % sec, ext_help, '.%s' %sec) )
__init_module_vars()

#############################################################################
def _map_std_arg_triples(callback, name_filter = lambda x : True):
    """Map `_std_arg_triples` via `callback`. This function is for internal
    use, it IS **NOT a part of public API**.

    :Parameters:
        callback : callable
            function of type ``callback(name, desc, default)``, where

                - ``name:`` is the name of variable being processed,
                - ``desc:`` is short description,
                - ``default:`` is the default value for the variable.
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``

    :Returns:
        the result of mapping the `_std_arg_triples` through the `callback`
    """
    triples = filter(lambda t : name_filter(t[0]), _std_arg_triples)
    return map(lambda x : callback(*x), triples)

#############################################################################
def ArgumentNames(name_filter = lambda x : True):
    """Return list of standard GNU directory argument names.

    :Parameters:
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
    :Returns:
        the list of standard GNU directory variable names
    """
    return _map_std_arg_triples(lambda *x : x[0], name_filter)

###############################################################################
def ArgumentDecls(**kw):
    """Return declarations of SCons *arguments* for all predefined GNU
    installation directory variables.

    :Keywords:
        defaults : dict
            User-specified default values for the Arguments being declared. You'll
            usually put your SCons Environment object env here,
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
        transformer : SConsArguments.Transformer
            a `SConsArguments.Transformer` object used to transform
            *argument* names to *endpoint* (construction variable, command-line
            variable, command-line option) names,
        env_key_prefix
            passed to `SConsArguments.Transformer.__init__()`,
        env_key_suffix
            passed to `SConsArguments.Transformer.__init__()`,
        env_key_transform
            passed to `SConsArguments.Transformer.__init__()`,
        var_key_prefix
            passed to `SConsArguments.Transformer.__init__()`,
        var_key_suffix
            passed to `SConsArguments.Transformer.__init__()`,
        var_key_transform
            passed to `SConsArguments.Transformer.__init__()`,
        opt_key_prefix
            passed to `SConsArguments.Transformer.__init__()`,
        opt_key_suffix
            passed to `SConsArguments.Transformer.__init__()`,
        opt_key_transform
            passed to `SConsArguments.Transformer.__init__()`, note that
            `ArgumentDecls` sets this to ``False`` by default,
        opt_prefix
            passed to `SConsArguments.Transformer.__init__()`,
        opt_name_prefix
            passed to `SConsArguments.Transformer.__init__()`,
        opt_name_suffix
            passed to `SConsArguments.Transformer.__init__()`,
        option_transform
            passed to `SConsArguments.Transformer.__init__()`.
    
    :Returns:
        an instance of `SConsArguments._ArgumentDecls`
    """
    def _callback(name, desc, default):
        try:
            default = defaults[name]
        except KeyError:
            pass
        if name.endswith('ext'):
            metavar = 'EXT'
        else:
            metavar = 'DIR'
        decl = { 'env_key'  : transformer.env_key_transform(name),
                 'var_key'  : transformer.var_key_transform(name),
                 'opt_key'  : transformer.opt_key_transform(name),
                 'default'  : default,
                 'help'     : desc,
                 'option'   : transformer.option_transform(name),
                 'type'     : 'string',
                 'nargs'    : 1,
                 'metavar'  : metavar }
        return name, decl

    defaults = kw.get('defaults', dict())
    name_filter = kw.get('name_filter', lambda s : True)
    try:
        transformer = kw['transformer']
    except KeyError:
        skip = ['defaults', 'name_filter', 'transformer', 'opt_key_transform']
        kw2 = { k:v for (k,v) in kw.iteritems() if k not in skip }
        # by default, we do not create options
        kw2['opt_key_transform'] = kw.get('opt_key_transform', False)
        transformer = SConsArguments.Transformer(**kw2)
    return SConsArguments.DeclareArguments(_map_std_arg_triples(_callback, name_filter))

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

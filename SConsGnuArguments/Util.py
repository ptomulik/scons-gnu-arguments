"""`SConsGnuArguments.Util`

Utility functions used by SConsGnuArguments
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
import SCons.Util

#############################################################################
def map_triples(callback, triples, name_filter = lambda x : True):
    """Map all predefined GNU variable triples (name, desc, default) via
    `callback`.

    :Parameters:
        callback : callable
            function of type ``callback(name, desc, default)``, where

                - ``name:`` is the name of variable being processed,
                - ``desc:`` is short description,
                - ``default:`` is the default value for the variable.
        triples : list
            a list of 3-element tuples with, each entry of the list should
            be a tuple of the form ``(name, desc, default)``, where ``name``
            is the name of argument, ``desc`` is description (used as help
            message) and ``default`` is default value.
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``

    :Returns:
        returns result of mapping through `callback`
    """
    if SCons.Util.is_Sequence(name_filter):
        seq = name_filter
        name_filter = lambda x : x in seq
    triples = filter(lambda t : name_filter(t[0]), triples)
    return map(lambda x : callback(*x), triples)

#############################################################################
def names_from_triples(triples, name_filter = lambda x : True):
    """Return list of argument names extracted from argument triples.

    :Parameters:
        triples : list
            a list of 3-element tuples with, each entry of the list should
            be a tuple of the form ``(name, desc, default)``, where ``name``
            is the name of argument, ``desc`` is description (used as help
            message) and ``default`` is default value.
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
    :Returns:
        the list of standard GNU directory variable names
    """
    return map_triples(lambda *x : x[0], triples, name_filter)

###############################################################################
def arguments_from_triples(triples, **kw):
    """Convert triples to argument declarations.

    :Parameters:
        triples : list
            a list of 3-element tuples with, each entry of the list should
            be a tuple of the form ``(name, desc, default)``, where ``name``
            is the name of argument, ``desc`` is description (used as help
            message) and ``default`` is default value.

    :Keywords:
        defaults : dict
            user-specified default values for the Arguments being declared,
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
        nameconv : `SConsArguments._ArgumentNameConv`
            a `SConsArguments._ArgumentNameConv` object used to transform
            *argument* names to *endpoint* (construction variable, command-line
            variable, command-line option) names,
        type
            create argument of given type (default: 'string')
        metavar
            use as command-line metavar
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
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
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
    # TODO: This is quite unorganized, I should get back here and elaborate
    def _callback(name, desc, default):
        try:
            default = defaults[name]
        except KeyError:
            pass
        if metavar:
            _metavar = metavar
        else:
            # FIXME: especially this, how do we know in general what the
            # metavar should we generate for a given variable, do we have any
            # idea? This should be probably job for _ArgumentNameConv.
            if name.endswith('ext'):
                _metavar = 'EXT'
            elif name.endswith('dir') or name == 'prefix' or name == 'exec_prefix':
                _metavar = 'DIR'
            else:
                _metavar = 'X'
        decl = { 'env_key'  : nameconv.env_key_transform(name),
                 'var_key'  : nameconv.var_key_transform(name),
                 'opt_key'  : nameconv.opt_key_transform(name),
                 'default'  : default,
                 'help'     : desc,
                 'option'   : nameconv.option_transform(name),
                 'type'     : _type,
                 'nargs'    : 1,
                 'metavar'  : _metavar }
        return name, decl

    defaults = kw.get('defaults', dict())
    name_filter = kw.get('name_filter', lambda s : True)
    _type = kw.get('type', 'string')
    metavar = kw.get('metavar')
    try:
        nameconv = kw['nameconv']
    except KeyError:
        skip = ['defaults', 'name_filter', 'nameconv', 'type', 'metavar']
        kw2 = { k:v for (k,v) in kw.iteritems() if k not in skip }
        nameconv = SConsArguments._ArgumentNameConv(**kw2)
    return SConsArguments.DeclareArguments(map_triples(_callback, triples, name_filter))

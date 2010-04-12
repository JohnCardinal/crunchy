# -*- coding: utf-8 -*-
"""
    pygments3.styles.borland
    ~~~~~~~~~~~~~~~~~~~~~~~

    Style similar to the style used in the Borland IDEs.

    :copyright: Copyright 2006-2009 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments3.style import Style
from pygments3.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class BorlandStyle(Style):
    """
    Style similar to the style used in the borland IDEs.
    """

    default_style = ''

    styles = {
        Whitespace:             '#bbbbbb',

        Comment:                'italic #008800',
        Comment.Preproc:        'noitalic #008080',
        Comment.Special:        'noitalic bold',

        String:                 '#0000FF',
        String.Char:            '#800080',
        Number:                 '#0000FF',
        Keyword:                'bold #000080',
        Operator.Word:          'bold',
        Name.Tag:               'bold #000080',
        Name.Attribute:         '#FF0000',

        Generic.Heading:        '#999999',
        Generic.Subheading:     '#aaaaaa',
        Generic.Deleted:        'bg:#ffdddd #000000',
        Generic.Inserted:       'bg:#ddffdd #000000',
        Generic.Error:          '#aa0000',
        Generic.Emph:           'italic',
        Generic.Strong:         'bold',
        Generic.Prompt:         '#555555',
        Generic.Output:         '#888888',
        Generic.Traceback:      '#aa0000',

        Error:                  'bg:#e3d2d2 #a61717'
    }

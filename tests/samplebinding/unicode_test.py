#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Shiboken Python Bindings Generator project.
#
# Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
#
# Contact: PySide team <contact@pyside.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 2.1 as published by the Free Software Foundation. Please
# review the following information to ensure the GNU Lesser General
# Public License version 2.1 requirements will be met:
# http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
# #
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA

'''Tests related to unicode'''

import unittest
import sys

import py3kcompat
import sample

class UnicodeAsConstCharArg(unittest.TestCase):

    def testUnicode(self):
        arg = py3kcompat.unicode('The Quick Brown Fox Jumps Over The Lazy Dog')
        self.assertEqual(sample.identity(arg), arg)

        # Default ascii codec can't encode this kind of string.
        if sys.getdefaultencoding() == 'ascii':
            arg = py3kcompat.unicode('\xc3\xa1', 'utf8')
            self.assertRaises(UnicodeEncodeError, sample.identity, arg)

if __name__ == '__main__':
    unittest.main()



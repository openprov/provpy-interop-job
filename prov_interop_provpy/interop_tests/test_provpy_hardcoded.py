"""Interoperability tests for ProvPy.
"""
# Copyright (c) 2015 University of Southampton
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions: 
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software. 
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 


from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from nose.tools import istest

from prov_interop import standards
from prov_interop_provpy.converter import ProvPyConverter
from prov_interop.interop_tests.test_converter import ConverterTestCase

@istest
class ProvPyHardCodedTestCase(ConverterTestCase):
  """Interoperability tests for ProvPy with a hard-coded configuration.
  """

  def setUp(self):
    super(ProvPyHardCodedTestCase, self).setUp()
    config = {}
    config[ProvPyConverter.EXECUTABLE] = "prov-convert"
    config[ProvPyConverter.ARGUMENTS] = "-f FORMAT INPUT OUTPUT"
    config[ProvPyConverter.INPUT_FORMATS] = [standards.JSON]
    config[ProvPyConverter.OUTPUT_FORMATS] = [standards.PROVX, standards.PROVN, standards.JSON]
    config[ConverterTestCase.SKIP_TESTS] = []

    self.converter = ProvPyConverter()
    super(ProvPyHardCodedTestCase, self).configure(config)

  def tearDown(self):
    super(ProvPyHardCodedTestCase, self).tearDown()

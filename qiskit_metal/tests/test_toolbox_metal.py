# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019-2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

#pylint: disable-msg=unnecessary-pass

"""
Qiskit Metal unit tests analyses functionality.

Created on  Wed Apr 22 09:59:02 2020
@author: Jeremy D. Drysdale
"""

import unittest

class TestToolboxMetal(unittest.TestCase):
    """
    Unit test class
    """

    def setUp(self):
        """
        Setup unit test

        Args: None

        Returns: None
        """
        pass

    def tearDown(self):
        """
        Tie any loose ends

        Args: None

        Returns: None
        """
        pass

    def test_toolbox_metal_test_a(self):
        """
        Test the functionality of A (replace this with a real test)

        Args: None

        Returns: None
        """
        self.assertEqual(1, 1)

    def test_toolbox_metal_test_b(self):
        """
        Test the functionality of B (replace this with a real test)

        Args: None

        Returns: None
        """
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

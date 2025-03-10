# test_password_validator.py

import unittest
from password_validator import is_password_secure

class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(is_password_secure("Valid1@Password"))

    def test_too_short(self):
        self.assertFalse(is_password_secure("Short1@"))

    def test_missing_special_character(self):
        self.assertFalse(is_password_secure("MissingSpecial1"))

    def test_missing_uppercase(self):
        self.assertFalse(is_password_secure("missing1@"))

    def test_missing_lowercase(self):
        self.assertFalse(is_password_secure("MISSING1@"))

    def test_missing_number(self):
        self.assertFalse(is_password_secure("MissingNumber@"))

    def test_all_conditions_met(self):
        self.assertTrue(is_password_secure("AllConditions1@"))

if __name__ == '__main__':
    unittest.main()
import unittest
from credential import credential


class TestCredentials(unittest.TestCase):
    def SetUp(self)

    self.new_credentials = Credential("Patrick","Buong","37897750","patrickbuong@gmail.com") # create account object


    def test_init(self):


        self.assertEqual(self.new_credential.credential_name,"Patrick")
        self.assertEqual(self.new_credential.user,"Buong")
        
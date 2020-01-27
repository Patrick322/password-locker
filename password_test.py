import unittest
from credential import credential


class TestCredentials(unittest.TestCase):
    def SetUp(self):

    self.new_credential = Credential("Patrick","Buong","37897750","patrickbuong@gmail.com") # create account object


    def test_init(self):


        self.assertEqual(self.new_credential.credential_name,"Patrick")
        self.assertEqual(self.new_credential.usr,"Buong")
        self.assertEqual(self.new_credential.password,"37897750")
        self.assertEqual(self.new_credential.email,"patrickbuong@gmail.com")

    def test_save_credential(self):

         self.new_credential.save_credential()
         self.assertEqual(len(Credential.credential_list),1)


    def tearDown(self):

        cedential.credential_list[]


    def test_save_multiple_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0797239875","user@.com")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
                    

    def test_delete_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential.credential("Test","user","0797239875","test@user.com")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_credential_name(self):
                    

        self.new_credential.test_save_credential()
        test_credential =Credential("Test","user","0797239875","test@user.com")
        test_credential.save_credential()

        found_credential = Credential.find_name_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)



    def test_credential_exists(self):


        self.new_credential.save_credential()
        test_Credential("Test","user","0797239875","test@user.com")
        test.credential.save_credential()

        credential_exists = Credential.credential_exist("0797239875")
        self.assertTrue(credential_exists)




     if__name__ == 'main__':
         unittest.main()           
import unittest
from main import app  # Az alkalmazás nevével importáljuk az app-et

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'Bark bark! Ready to roll.')

    def test_get_counter(self):
        response = self.app.get('/counter')  # testing data retrival from server
        self.assertEqual(response.status_code, 200)
  

    #def test_update_counter(self):
    #    payload = {'counter': 1234}  # Az elküldendő adatok
    #    response = self.app.post('/', json=payload)
    #    self.assertEqual(response.status_code, 200)
    #    # Tesztelés az új érték beállításának sikerességére és a válaszra

if __name__ == '__main__':
    unittest.main()

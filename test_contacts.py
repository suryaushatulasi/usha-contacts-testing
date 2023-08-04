import unittest
from flask import Flask, jsonify
from apps.app import app


class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client using Flask's testing utilities
        self.app = app.test_client()

        # Enable Flask's testing mode
        app.testing = True

    def test_get_contacts_positive(self):
        response = self.app.get('/contacts')
        self.assertEqual(response.status_code, 200)
        contacts = response.get_json()

        self.assertIsInstance(contacts, list)

    def test_get_contact_list_positive(self):
        response = self.app.get('/contact-list')
        self.assertEqual(response.status_code, 201)
        contacts = response.get_json()
        self.assertIsInstance(contacts, list)
        self.assertEqual(contacts[1], {'id': 2, 'name': 'tulasi', 'ph_no': 2345678901})
        self.assertEqual(contacts[1]['name'], 'tulasi')

    def test_get_contact_list_negative(self):
        response = self.app.get('/contact-list')
        self.assertNotEqual(response.status_code, 200)
        contacts = response.get_json()
        self.assertIsInstance(contacts, list)
        self.assertNotEqual(contacts[0], {'id': 2, 'name': 'usha', 'ph_no': 1234567890})
        self.assertNotEqual(contacts[0]['name'], 'usha2')

    def test_add_contact(self):
        new_contact = {'name': 'rk', 'ph_no': 9876543213}
        response = self.app.post('/insert-contact', json=new_contact)
        self.assertEqual(response.status_code, 201)
        created_contact = response.get_json()
        self.assertIsInstance(created_contact, dict)
        self.assertEqual(created_contact, {'id': 5, 'name': 'rk', 'ph_no': 9876543213})
        self.assertEqual(created_contact['name'], new_contact['name'])
        self.assertEqual(created_contact['ph_no'], 9876543213)
        self.assertEqual(created_contact['id'], 5)

    def test_update_contact(self):
        contact_id = 1
        updated_contact = {'name': 'karthik'}
        response = self.app.put(f'/contacts/{contact_id}', json=updated_contact)
        self.assertEqual(response.status_code, 200)
        updated_contact_response = response.get_json()
        self.assertIsInstance(updated_contact_response, dict)  # Here we will get dictionary so we mentioned dict

        self.assertEqual(updated_contact_response['name'], updated_contact['name'])

    def test_delete_contact(self):
        contact_id = 1
        response = self.app.delete(f'/contacts/{contact_id}')
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['msg'], '1 contact has been deleted')


if __name__ == '__main__':
    unittest.main()

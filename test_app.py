import os
import unittest
import json
import os
from flask_sqlalchemy import SQLAlchemy

from models import setup_db, Person, Artical
from app import create_app

admin_token = os.getenv('ADMIN_TOKEN')
admin_tokenn = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjI1MjA1MiwiZXhwIjoxNTkyMzM4NDUyLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.mwS6FH1HZqjl-Vdm_642bOXWCRYpt0fJTD9OE1lyfJilrfJrMS368Q5cccPwTddQV_4IxFDD5WnD3Cs83I4B-7wr0et0VqHolekpRpbQRT8SeGNkN7L1a66wNzywpvhc3Z2ktOJVbQzhmyaPO8ooXwxUi7TRi5q9615i7jfLEPUzyk0gf6CgvYxK-vZqxuyoLjKLXcI4gnlw_gXdMqUw9h5kOCLqh9MQ6HyJ_9JOquWGnSbiT1HuYMW2v6pS5drkilbnH6ab_hn7APS30BOqEV-8L14QpsunBJHbPoP2oAf6gq7t6ZjjrPlPDlYii-tqqi7NqLvOQ2C_kzEZJEu8Zw"



# class for unit tesst
class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    # funtion for setup our database

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "areeg"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'areeg', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # new question for test
        self.new_questions = {
            'question': 'Anansi Boys',
            'answer': 'Neil Gaiman',
            'category': 1,
            'difficulty': 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # use for test all category if return 200 and so on
    def test_get_person(self):
        res = self.client().get('/person', headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['person'])
        self.assertEqual(data['success'], True)

    def test_get_person_error(self):
        res = self.client().get('/person', headers = '')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_article(self):
        res = self.client().get('/article', headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['articles'])
        self.assertEqual(data['success'], True)

    def test_get_article_error(self):
        res = self.client().get('/article', headers ='')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_post_person(self):
        person = {
            "name":"AREEEEEEEEGOOOOOOOOOO",
            "department":"NNNNNNNNEEEEEEETTTWWWORRK",
            "id":94

        }
        res = self.client().post('/person', json = person,  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['person'])
        self.assertEqual(data['success'], True)

    def test_post_person_error(self):

        res = self.client().post('/person', json = {},  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_article(self):
        article = {
            "data":"AREEEEEEEEGOOOOOOOOOO",
            "category":"NNNNNNNNEEEEEEETTTWWWORRK",
            "person_id":3,
            "id":94
        }
        res = self.client().post('/article', json = article,  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['article'])
        self.assertEqual(data['success'], True)

    def test_post_article_error(self):

        res = self.client().post('/article', json = {},  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch_person(self):
        person = {
            "name":"tessssssssssssssssst" 
        }

        res = self.client().patch('/person/27', json = person,  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['persons'])
        self.assertEqual(data['success'], True)


    def test_patch_person_error(self):

        res = self.client().patch('/person/3', json = {},  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch_article(self):
        article = {
            "data":"tessssssssssssssssst" 
        }

        res = self.client().patch('/article/4', json = article,  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['articles'])
        self.assertEqual(data['success'], True)


    def test_patch_article_error(self):

        res = self.client().patch('/article/4',  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_delete_person(self):

        res = self.client().delete('/person/94',  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_id'])
    
    def test_delete_person_error(self):

        res = self.client().delete('/person/1234',  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    

    def test_delete_article(self):

        res = self.client().delete('/article/9',  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_id'])
    
    def test_delete_article_error(self):

        res = self.client().delete('/atricle/1234',  headers = {'Authorization': 'Bearer {}'.format(admin_tokenn)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)







if __name__ == "__main__":
    unittest.main()

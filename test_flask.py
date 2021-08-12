from unittest import TestCase
from app import app
from models import db, User


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views for Users"""

    def setUp(self) -> None:
        """Add sample user"""

        User.query.delete()

        user = User(first_name="Test", last_name="User",
                    image_url="https://static.thenounproject.com/png/2884221-200.png")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self) -> None:
        """Clean up"""
        db.session.rollback()

    def test_users_list(self):
        with app.test_client() as client:
            res = client.get("/users")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Test User', html)

    def test_show_user(self):
        with app.test_client() as client:
            res = client.get(f"/users/{self.user_id}")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<h5 class="card-title">Test User</h5>', html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "Test", "last_name": "User2",
                 "image_url": "https://static.thenounproject.com/png/2884221-200.png"}
            res = client.post("/users/new", data=d, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('>Test User2</a>', html)

    def test_edit_form(self):
        with app.test_client() as client:
            res = client.get(f"/users/{self.user_id}/edit")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<h1>Edit User</h1>', html)

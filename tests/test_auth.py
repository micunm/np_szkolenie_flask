from app.auth.models import User
from tests.conftest import FlaskBaseTest


class TestAuth(FlaskBaseTest):
    def test_create_user(self):
        response = self.client.post('/admin/', data={
            'name': 'username',
            'email': 'foo@bar.baz',
            'password1': 'one',
            'password2': 'one',
        })
        assert response.status_code == 302

        assert User.query.count() == 1
        assert User.query.first().email == 'foo@bar.baz'

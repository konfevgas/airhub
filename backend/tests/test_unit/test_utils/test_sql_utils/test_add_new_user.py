from app.database.connection import get_db
from app.database.models import Users
from app.utils.sql_utils import add_new_user

session = next(get_db())


def test_add_new_user() -> None:
    """
    Test the add_new_user function to verify it correctly adds a new user to the database.
    """
    new_user = add_new_user(
        user_data=Users(id=2, email="test@example.com", full_name="Test User"),
        session=session,
    )
    assert new_user.email == "test@example.com"

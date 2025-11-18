from app.database.connection import get_db
from app.utils.sql_utils import check_user_exists

session = next(get_db())


def test_check_user_exists() -> None:
    """
    Test the check_user_exists function to verify it correctly identifies existing users.
    """
    user_exists = check_user_exists(user_email="fesas198@gmail.com", session=session)
    assert user_exists is True

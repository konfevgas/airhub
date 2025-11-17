from app.database.connection import get_db
from app.utils.sql_utils import check_user_exists

session = next(get_db())


def test_check_user_exists() -> None:
    user_exists = check_user_exists(user_email="fesas1988@gmail.com", session=session)
    assert user_exists is True

from sqlalchemy.orm import Session

from app.database.models import Users


def check_user_exists(user_email: str, session: Session) -> bool:
    """
    Check if a user with the given email exists in the database.

    Args:
        user_email (str): The email of the user to check.
        session (Session): The database session.

    Returns:
        bool: True if the user exists, False otherwise.
    """
    email_exists = session.query(Users).filter(Users.email == user_email).first()
    return True if email_exists else False


def add_new_user(user_data: Users, session: Session) -> Users:
    """
    Create a new user to the database and return the created user.

    Args:
        user_data (Users): A Users object containing user information.
        session (Session): The database session.

    Returns:
        Users: The created user object.
    """
    new_user = Users(
        email=user_data.email,
        full_name=user_data.full_name,
        is_active=True,
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

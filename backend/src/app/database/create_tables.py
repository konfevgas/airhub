from loguru import logger

from app.database.connection import Base, engine
from app.database.models import Airports

logger.info("Creating tables...")
Base.metadata.create_all(bind=engine)
logger.info("Done.")

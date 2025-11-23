import csv
from pathlib import Path

from loguru import logger

from app.database.connection import SessionLocal
from app.database.models import Airports

CSV_PATH = Path("C:/Users/fesas/temp/airhub_data/airports.csv")


def parse_int(v: str):
    v = v.strip()
    return int(v) if v not in ("", r"\N") else None


def parse_float(v: str):
    v = v.strip()
    return float(v) if v not in ("", r"\N") else None


def parse_str(v: str):
    v = v.strip().strip('"')
    return v if v not in ("", r"\N") else None


def load_airports():
    logger.info(f"Loading airports from {CSV_PATH}")

    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

    db = SessionLocal()

    try:
        with CSV_PATH.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)

            airports = []

            for row in reader:
                airport = Airports(
                    id=parse_int(row[0]),
                    name=parse_str(row[1]),
                    city=parse_str(row[2]),
                    country=parse_str(row[3]),
                    iata=parse_str(row[4]),
                    icao=parse_str(row[5]),
                    latitude=parse_float(row[6]),
                    longitude=parse_float(row[7]),
                    elevation=parse_int(row[8]),
                    utc_offset=parse_float(row[9]),
                    dst=parse_str(row[10]),
                    timezone=parse_str(row[11]),
                    airport_type=parse_str(row[12]),
                    source=parse_str(row[13]),
                    # created_at → auto-filled by DB
                )
                airports.append(airport)

        db.add_all(airports)
        db.commit()

        logger.info(f"Inserted {len(airports)} airports successfully.")

    except Exception as e:
        db.rollback()
        logger.exception(f"Failed to load airports: {e}")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    load_airports()

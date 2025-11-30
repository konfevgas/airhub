from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Airports
from app.schemas.list_airports import ListAirportsReponse

router = APIRouter()


@router.post("/list_airports")
async def list_airports(
    query: str | None = Query(default=None, description="Search by name, city, country, IATA, ICAO"),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    sort_by: str | None = Query(
        default="name", pattern="^(name|country)$", description="Sort results by name or country"
    ),
    db_session: Session = Depends(get_db),
) -> ListAirportsReponse:
    """
    Route to list airports.

    Args:
        query (str | None): The search query.
        limit (int): The maximum number of results to return.
        offset (int): The number of results to skip.
        sort_by (str | None): The field to sort results by.
        db_session (Session): The database session.

    Returns:
        List[ListAirportsReponse]: A list of airports matching the query.
    """
    query = db_session.query(Airports)

    # --------- Filtering ---------
    if query:
        q_like = f"%{query}%"
        query = query.filter(
            (Airports.name.ilike(q_like))
            | (Airports.city.ilike(q_like))
            | (Airports.country.ilike(q_like))
            | (Airports.iata.ilike(q_like))
            | (Airports.icao.ilike(q_like))
        )

    # --------- Sorting ---------
    if sort_by == "name":
        query = query.order_by(Airports.name.asc())
    elif sort_by == "country":
        query = query.order_by(Airports.country.asc())

    # --------- Pagination ---------
    airports = query.offset(offset).limit(limit).all()

    return airports

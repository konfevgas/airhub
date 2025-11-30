from pydantic import BaseModel


class ListAirportsReponse(BaseModel):
    id: int
    name: str
    city: str
    country: str
    iata: str | None
    icao: str | None
    latitude: float
    longitude: float
    altitude: int | None
    timezone: str | None

    class Config:
        from_attributes = True  # important for ORM

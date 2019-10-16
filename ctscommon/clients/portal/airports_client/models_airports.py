from pydantic import BaseModel


class AirportBase(BaseModel):
    AirportCode: str
    AirportName: str
    CityCode: str
    CityName: str
    CountryCode: str
    CountryName: str
    RegionName: str
    SabreRegionName: str = None


class AirportUpdateSchema(BaseModel):
    AirportCode: str = None
    AirportName: str = None
    CityCode: str = None
    CityName: str = None
    CountryCode: str = None
    CountryName: str = None
    RegionName: str = None
    SabreRegionName: str = None
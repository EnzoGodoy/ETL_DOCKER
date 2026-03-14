import os 
from dataclasses import dataclass

@dataclass
class Settings:
    api_base_url: str = os.getenv("api_base_url","https://api.openbrewerydb.org/v1/breweries")
    db_host: str = os.getenv("db_host")
    db_port: int = os.getenv("db_port",5432)
    db_name: str = os.getenv("db_name", "etl_db")
    db_user: str = os.getenv("db_user", "etl_user")
    db_password: str = os.getenv("db_password", "etl_pass")
    per_page: int = os.getenv("per_page", 50)
    max_pages: int = os.getenv("max_pages", 5)


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Config class for the application settings."""
    app_name: str = "Sample Application"
    debug: bool = False
    # connection string for the database
    host: str = "localhost"
    port: int = 5432
    username: str = "user"
    password: str = "password"
    database: str = "sample"
    
    @property
    def database_url(self) -> str:
        """Construct the database URL from the individual components."""
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

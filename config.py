from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_port: int
    database_name: str
    algorithm: str
    secret_key: str
    access_token_expire_minutes: int
    class Config:
        env_file = '.env'

settings = Settings()

if __name__ == '__main__':
    print(settings.database_name)

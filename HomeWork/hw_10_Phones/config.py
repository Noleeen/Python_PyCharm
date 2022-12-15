from pydantic import BaseSettings, SecretStr

class Setting(BaseSettings):
    bot_token: SecretStr
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

config = Setting
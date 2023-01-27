

class BaseConfig:
    # for now this can stay here, no super evil harm can be done with it
    SENTRY_DSN: str = ""
    NAME: str = ""
    ENV: str = "dev_local"
    API_PORT: int = 0

from loguru import logger

logger.add(
    "./logs/log_file.log",
    rotation="1 day",
    level="DEBUG",
    retention="5 days",
    backtrace=True,  # if ENVIRONMENT == ENV_PROD else True,
    diagnose=True,  # if ENVIRONMENT == ENV_PROD else True,
)
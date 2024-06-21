import uvicorn
from dotenv import load_dotenv

from isheet.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    load_dotenv()
    uvicorn.run(
        "isheet.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()

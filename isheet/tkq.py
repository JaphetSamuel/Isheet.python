import taskiq_fastapi
from taskiq import InMemoryBroker, ZeroMQBroker

from isheet.settings import settings

broker = ZeroMQBroker()

if settings.environment.lower() == "pytest":
    broker = InMemoryBroker()

taskiq_fastapi.init(
    broker,
    "isheet.web.application:get_app",
)

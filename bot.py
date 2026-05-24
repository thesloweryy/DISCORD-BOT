from __future__ import annotations

from pathlib import Path

from golden_shadow_bot.config import settings
from golden_shadow_bot.database import Database
from golden_shadow_bot.discord_bot import GoldenShadowBot
from golden_shadow_bot.logging_config import setup_logging
from golden_shadow_bot.services import BotServices
from golden_shadow_bot.trucky import TruckyClient


def main() -> None:
    setup_logging(settings.log_level)
    db = Database(settings.database_path)
    trucky = TruckyClient(
        settings.trucky_api_base_url,
        settings.trucky_company_id,
        settings.trucky_api_token,
        settings.trucky_user_agent,
    )
    services = BotServices(db, trucky, Path("data"))
    bot = GoldenShadowBot(settings, services)
    bot.run(settings.discord_token)


if __name__ == "__main__":
    main()
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection
from alembic import context
from database import Model

# Загружаем конфиг Alembic
config = context.config

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываем MetaData, чтобы Alembic мог отслеживать изменения моделей
target_metadata = Model.metadata

# URL базы данных
DATABASE_URL = "postgresql+asyncpg://postgres:moggerisme@localhost/fastapi_test_db"


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме (без подключения к БД)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме (с подключением к БД)."""
    engine = create_async_engine(DATABASE_URL, echo=True)

    async with engine.begin() as connection:
        await connection.run_sync(do_migrations)


def do_migrations(connection: AsyncConnection):
    """Функция для выполнения миграций в синхронном контексте."""
    context.configure(
        connection=connection, target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())

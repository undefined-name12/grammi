import os
import sys
import asyncio
import logging
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command
from src.bot.core.aiobot import AioBot
from src.database.db_adapter import DBAdapter

logging.basicConfig(level=logging.INFO,
                    stream=sys.stderr,
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()
bot_token: str|None = os.environ.get("BOT_TOKEN")

if not bot_token:
    logging.error("The environment variable BOT_TOKEN hasn't been found. \
                  Make sure you are running your docker container as follows: \
                  docker run -e BOT_TOKEN=\"YOUR_BOT_TOKEN\" \
                  --name tgrambuddy-container -d tgrambuddy-app ")    
    exit(1)

def run_migrations():
    try:
        # 1. Create folder if not exists
        db_path = Path("data/database")
        db_path.mkdir(parents=True, exist_ok=True)
        
        # 2. Initi db_adapter
        db_adapter = DBAdapter(db_engine='sqlite')
        
        # 3. Apply migrations
        subprocess.run(["alembic", "upgrade", "head"], check=True)
       
        return db_adapter
        
    except Exception as e:
        logging.error(f"Database initialization failed: {e}")
        raise
    
async def main(db_adapter: DBAdapter):
    logging.info(f"Runing bot with. BOT_TOKEN:{bot_token}")
    
    try:        
        bot_instance = AioBot(token=bot_token, logging=logging, db_adapter=db_adapter)
        await bot_instance.run()
    finally:
        await db_adapter.close()

if __name__ == "__main__":
    # Init database
    logging.info(f'DB_ROOT: {os.getenv("DB_ROOT")}')
    logging.info(f'ASYNCSQLITE_DB_URL: {os.getenv("ASYNCSQLITE_DB_URL")}')
    db_adapter = run_migrations()
    logging.info("Database initialized successfully")
    
    asyncio.run(main(db_adapter))

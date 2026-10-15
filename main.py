
from loguru import logger
from app.asgi import app

# Vercel needs a top-level FastAPI instance named "app"

if __name__ == "__main__":
    import uvicorn
    from app.config import config

    logger.info(
        f"Starting server, docs: http://127.0.0.1:{config.listen_port}/docs"
    )

    uvicorn.run(
        app,
        host=config.listen_host,
        port=config.listen_port,
        reload=config.reload_debug,
        log_level="warning",
    )

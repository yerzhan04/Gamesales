import os

from fastapi import Header, HTTPException


def load_env():
    import os
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)


load_env()


async def get_token_header(token: str = Header()):
    if token != os.environ.get('token'):
        raise HTTPException(status_code=400, detail="Token header invalid")

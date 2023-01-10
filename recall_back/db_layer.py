from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("postgresql://recall_server_db_user:recall_server_db_user_test_pwd@localhost:5432/postgres",
                       echo=True)


def get_user(uid: str) -> str:
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        val = result.all()[0][0]
        return val

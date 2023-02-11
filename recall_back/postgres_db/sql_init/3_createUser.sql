-- TODO: security; restrict rights to select/update/delete/insert

CREATE USER recall_server_db_user PASSWORD 'recall_server_db_user_test_pwd';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA recall_db_schema TO recall_server_db_user;
GRANT ALL PRIVILEGES ON SCHEMA recall_db_schema TO recall_server_db_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA recall_db_schema TO recall_server_db_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA recall_db_schema TO recall_server_db_user;

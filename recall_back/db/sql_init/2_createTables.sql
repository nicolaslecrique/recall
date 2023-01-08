-- All tables has
-- id: primary_key, int, for join requests and foreign keys, should not be exposed to service clients
-- uri: unique identifier, immutable, can be exposed
-- creation_datetime: for diagnostics


CREATE TABLE recall_db_schema.user_account(
   id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
   uri TEXT NOT NULL UNIQUE,
   firebase_auth_uid TEXT NOT NULL UNIQUE, -- for connection
   creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE recall_db_schema.workspace(
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    uri TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE recall_db_schema.workspace_member(
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    workspace_id BIGINT NOT NULL REFERENCES recall_db_schema.workspace(id),
    user_account_id BIGINT NOT NULL REFERENCES recall_db_schema.user_account(id),
    creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    UNIQUE(workspace_id, user_account_id)
);


CREATE TABLE recall_db_schema.item(
  id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  uri TEXT NOT NULL UNIQUE,
  workspace_id BIGINT NOT NULL REFERENCES recall_db_schema.workspace(id),
  created_by BIGINT NOT NULL REFERENCES recall_db_schema.workspace_member(id),
  creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);



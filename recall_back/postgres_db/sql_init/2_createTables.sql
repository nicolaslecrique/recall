-- All tables has
-- id: primary_key, int, for join requests and foreign keys, should not be exposed to service clients
-- uri: unique identifier, immutable, can be exposed
-- creation_datetime: for diagnostics


CREATE TABLE recall_db_schema.user(
   id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
   firebase_auth_uid TEXT NOT NULL UNIQUE, -- for connection
   email TEXT NOT NULL UNIQUE,
   creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE recall_db_schema.workspace(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE recall_db_schema.workspace_member(
    workspace_id uuid NOT NULL REFERENCES recall_db_schema.workspace(id),
    user_id uuid NOT NULL REFERENCES recall_db_schema.user(id),
    creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY(workspace_id, user_id)
);


CREATE TABLE recall_db_schema.item(
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  title TEXT NOT NULL,
  text_content TEXT NOT NULL,
  last_modification_datetime TIMESTAMPTZ NOT NULL,
  workspace_id uuid NOT NULL REFERENCES recall_db_schema.workspace(id),
  creator_id uuid NOT NULL REFERENCES recall_db_schema.user(id),
  creation_datetime TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);



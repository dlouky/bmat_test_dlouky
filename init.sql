ALTER ROLE dlouky SET client_encoding TO 'utf8';
ALTER ROLE dlouky SET default_transaction_isolation TO 'read committed';
ALTER ROLE dlouky SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dlouky TO dlouky;
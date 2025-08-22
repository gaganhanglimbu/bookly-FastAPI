>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          psql -h localhost -U postgres -d bookly_db                 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
connect database





Alembic is a database migration tool for Python, most commonly used with SQLAlchemy (the ORM used in FastAPI, Flask, etc.).
What it does

Tracks changes you make to your database models (tables, columns, constraints, etc.).

Generates migration scripts (Python scripts that modify the database schema).

Lets you upgrade (apply new changes) or downgrade (revert changes) the database schema.


>>>>>>>>>>>>>>>>>>>>>>>>>>>>         alembic init -t async migrations         <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
alembic init → sets up a brand-new Alembic environment.

-t async → tells Alembic to create an environment template that supports async SQLAlchemy (for projects using async_engine in FastAPI, etc.).

migrations → the folder name where migration files will live.




>>>>>>>>>>>>>>>>>>>>>>>>>>>            alembic revision --autogenerate -m 'init'        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
alembic revision → creates a new migration script (like makemigrations in Django).

--autogenerate → tells Alembic to compare your current database schema with your SQLAlchemy models and automatically generate the necessary changes.

-m 'init' → a message to label the migration (just like Django migration filenames include descriptions).





>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             alembic upgrade head               <<<<<<<<<<<<<<<<<<<<<<<<<
upgrade → tells Alembic to apply migrations in the upgrade direction (opposite of downgrade).

head → means “the latest revision” (the newest migration script in migrations/versions/).











>>>>>>>>>>>>>>>>>>>>>>>>>>>>> pip install passlib <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

You’re installing Passlib, a Python password hashing library.

🔹 What it does

Provides secure password hashing algorithms (bcrypt, argon2, pbkdf2, sha512_crypt, etc.).

Makes it easy to hash and verify passwords (instead of storing plain text passwords).

Used in frameworks like FastAPI, Flask, Pyramid for authentication systems.



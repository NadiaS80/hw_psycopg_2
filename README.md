# PostgreSQL Client Manager (Python + psycopg2)  
Simple, clean program to manage clients and their phone numbers in PostgreSQL. Built for a homework assignment, but structured like a tiny real project. ✨

---

## 🧩 Project Structure

```
├── DB_Settings.py   // Connection handling (open cursor, commit, close)
├── DB_Create.py     // Schema creation: Client, Phone (with ON DELETE CASCADE)
├── DB_Control.py    // Core CRUD: add client/phone, update, delete, find
└── run_cod.py       // Entry point with runnable demo (if __name__ == '__main__')
```

**What each module does, in plain English:**
- **DB_Settings.py** — a base class that opens a PostgreSQL connection and provides helpers for cursor/commit/close. Other classes inherit it to share the same connection workflow.  
- **DB_Create.py** — creates two tables:
  - `Client` (first_name, last_name, email)
  - `Phone` (number, client_id → references Client with `ON DELETE CASCADE`)
- **DB_Control.py** — core operations:
  - `insert_Client(first_name, last_name, email)` → returns `id`
  - `insert_Phone(number, client_id)`
  - `update_Client(id, first_name=None, last_name=None, email=None)`
  - `delete_Phone(client_id, number)`
  - `delete_Client(id)` (phones are removed automatically via cascade)
  - `find_Client(first_name=None, last_name=None, email=None, number=None)` → returns dict or `None`
- **run_cod.py** — executable example showing how to create tables, insert/update/delete, and query data.

> Heads-up: table names are capitalized (`Client`, `Phone`) in SQL for the assignment’s style. In production, snake_case is more conventional.

---

## ⚙️ Requirements

```
psycopg2==2.9.9
```

Install with:

```
pip install -r requirements.txt
```

---

## 🗄️ Database Prep
Make sure PostgreSQL is running and you have a database created (use your own name/password).  
If needed, create a database:

```
createdb YOUR_DB_NAME
```

Optional (connect via psql and create a user, if you don’t use the default `postgres`):

```
psql -d YOUR_DB_NAME
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE "YOUR_DB_NAME" TO your_user;
```

---

## 🔑 Configuration
Open **run_cod.py** and set your database name and password:

```
database = 'YOUR_DB_NAME'
password = 'YOUR_PASSWORD'
```

If your setup isn’t local defaults, extend the connection in `DB_Settings.py` with host/port (e.g., `host='localhost', port=5432`).

---

## ▶️ How to Run

1) Create tables (automatically done when you run the script):

```
python run_cod.py
```

2) The script will:
- create tables `Client` and `Phone` (if not exist),
- insert demo clients (Pavel Durov, Guido van Rossum),
- attach phones,
- update/delete some data,
- run a sample search.

You can tweak the demo in **run_cod.py** to test different scenarios.

---

## 🔍 Query Behavior (find_Client)
`find_Client` builds a dynamic filter from any of these fields: `first_name`, `last_name`, `email`, `number`.  
It returns:
- a dict with `id`, `first_name`, `last_name`, `email`, and `numbers` (list of phones), or  
- `None` if nothing matches.

Example usage inside `run_cod.py`:

```
print(client_2.find_Client(last_name='van Rossum'))
```

---

## 🧯 Safety & Notes
- Parameterized queries are used for values. For updating column names (`update_Client`), keep the internal whitelist approach or switch to `psycopg2.sql.Identifier` for production-grade safety.
- `ON DELETE CASCADE` ensures when a client is removed, all related phones go with them. Less cleanup, fewer tears. 😅
- If you change table names/columns, make sure to update all SQL snippets consistently.

---

## 📜 License
MIT License

---

## ✍️ Author’s Note
Last time the joke was “SQL made me cry.” This time it’s different:  
**PostgreSQL didn’t break my heart — it just asked for a COMMIT first.** 💍🚀

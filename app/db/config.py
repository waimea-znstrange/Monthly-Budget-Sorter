#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class CatTable:

    NAME = "categories"

    SCHEMA = """
        CREATE TABLE categories (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            notes   TEXT,
            budget  INTEGER DEFAULT 0
        )
    """

    SEED_DATA = """
        INSERT INTO categories (name, notes, budget)
        VALUES
            ("Food", "", 200),
            ("Fun", "", 100)
    """

class SpendTable:

    NAME = "spending"

    SCHEMA = """
        CREATE TABLE spending (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            date    TEXT NOT NULL,
            cat_id  INTEGER NOT NULL,
            name    TEXT NOT NULL,
            amount  INTEGER DEFAULT 0,

            FOREIGN KEY (cat_id) REFERENCES categories(id)
        )
    """

    SEED_DATA = """
        INSERT INTO spending (date, cat_id, name, amount)
        VALUES
            ("2026-09-01", 1, "Lunch at Maccas", 20),
            ("2026-09-01", 2, "Bet of the horses", 50)
    """




#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    CatTable,
    SpendTable,
]


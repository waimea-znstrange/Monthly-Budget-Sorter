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

class AccountTable:

    NAME = "account"

    SCHEMA = """
        CREATE TABLE account (
            id      BIGINT,
            date    TEXT,
            category_id    INTEGER,
            name    TEXT,
            amount  INTEGER
        )
    """

    SEED_DATA = """
        INSERT INTO account (name, category_id, amount)
        VALUES
            ("name",  1, "Groceries"),
            ("category_id",  0, "category_id"),
            ("amount",  0, "$200")
    """

# Add more table classes here...



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
    AccountTable,
    # Add more tables here...
]


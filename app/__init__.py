#===========================================================
# Monthly-Budget-Sorter Project
# By Zeb
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================


#-----------------------------------------------------------
# Menu page - Greeting
#-----------------------------------------------------------
@app.get("/")
def show_menu():

        flash("Test message")
        flash("Test SUCCESS message", "success")
        flash("Test INFO message", "info")
        flash("Test WARNING message", "warning")
        flash("Test ERROR message", "error")

        params = ()
        cat_data = db.execute(sql, params).fetchall()


#-----------------------------------------------------------
# Home page - Show all categories
#-----------------------------------------------------------
@app.get("/cat_list")
def show_categories():
    with connect_db() as db:
        sql = """
            SELECT 
                categories.name,
                categories.budget,
                SUM(spending.amount) [- budget] AS total

            FROM categories
            JOIN spending ON spending.cat_id = categories.id

            GROUP BY categories.name
            
            ORDER BY name ASC
        """
        params = ()
        cat_data = db.execute(sql, params).fetchall()

        return render_template("pages/cat_list.jinja", cat_data=cat_data)


#-----------------------------------------------------------
# Timeline - Show timeline
#-----------------------------------------------------------
@app.get("/timeline")
def show_timeline():
    with connect_db() as db:
        sql = """
            SELECT
                spending.date,
                spending.reason,
                spending.amount

            FROM spending

            ORDER BY spending.date ASC
        """
        params = ()
        cat_data = db.execute(sql, params).fetchall()

        return render_template("pages/timeline.jinja", cat_data=cat_data)


#-----------------------------------------------------------
# Get Category Form - Add categories page
#-----------------------------------------------------------
@app.get("/add_cat")
def add_categories():
    with connect_db() as db:
        sql = """
            SELECT
                categories.name,
                categories.notes,
                categories.budget

            FROM categories

            ORDER BY categories.name ASC
        """
        params = ()
        cat_data = db.execute(sql, params).fetchall()

        return render_template("pages/add_cat.jinja", cat_data=cat_data)


#-----------------------------------------------------------
# Post Category form - Add categories page
#-----------------------------------------------------------
@app.post("/add_cat")
def post_categories():
    with connect_db() as db:
        sql = """
            SELECT
                categories.name,
                categories.notes,
                categories.budget

            FROM categories

            ORDER BY categories.name ASC
        """
        params = ()
        cat_data = db.execute(sql, params).fetchall()

        return render_template("pages/add_cat.jinja", cat_data=cat_data)



#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)


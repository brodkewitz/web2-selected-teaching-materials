from flask import Flask, render_template, request

# A simple dynamic web app using Flask.
#
# Users can view the current list of names, and add a new one by submitting
# a GET request with a ?name parameter. Names are stored in a file on disk.
#
# To run:
# $ source venv/bin/activate
# $ pip install -r requirements.txt
# $ python3 ./names.py
# Dev server configured for port 8000 and 0.0.0.0 external access,
# configured in if-main
# NOTE: 221116 There's a bug in the flask CLI command where the --host
# option is missing (despite the documentation for 2.2.x AND 2.1.x).


app = Flask(__name__)


def get_names_list():
    """Retrieve list of names from the file. Returns a list."""
    with open("names.txt", "r") as f:
        names_list = [line.strip() for line in f.readlines()]
        return names_list


def append_new_name(name):
    """Append the given name to the names list.
       Returns an updated names list."""
    with open("names.txt", "r+") as f:
        f.seek(0, 2) # Seek to end of file
        f.write(f"{name}\n")
        f.seek(0) # Seek to beginning of file
        names_list = [line.strip() for line in f.readlines()]
        return names_list


@app.route("/")
def index():
    print(f"\nNew request, user agent: {request.headers['User-Agent']}")
    name = request.args.get("name", "")
    names_list = get_names_list()
    if not name:
        return render_template("index.html",
                               name="",
                               names_list=names_list,
                               name_exists=False)
    if name and name in names_list:
        return render_template("index.html",
                               name=name,
                               names_list=names_list,
                               name_exists=True)
    if name and name not in names_list:
        names_list = append_new_name(name)
        return render_template("index.html",
                               name=name,
                               names_list=names_list,
                               name_exists=False)












# Add a minimal API component with HTTP + json + CRUD functionality.
# This is a very simple RESTful API using native HTTP methods.
#
# Note: This is bad structure for a typical Python script. Imports and
# functions have been rearranged to move all api-related code "below the
# fold" for demo purposes.


import json


# Write the rest of the CRUD functions

def update_name(name, new_name, names_list):
    """Update the given name with a new_name. This assumes we've already
       checked that the name is in the list and that renaming the entry
       won't conflict with an existing one.

       Updating the name in the file is done by overwriting the entire
       file's previous contents.
    
       Returns an updated names list."""
    name_id = names_list.index(name)
    names_list[name_id] = new_name
    with open("names.txt", "w+") as f:
        for n in names_list:
            f.write(f"{n}\n")
        f.seek(0)
        names_list = [line.strip() for line in f.readlines()]
        return names_list


def delete_name(name, names_list):
    """Delete the given name from the names list. This assumes we've
       already checked whether the name exists.
       
       Removing the name from the file is done by overwriting the entire
       file's previous contents.

       Returns an updated names list."""
    names_list.remove(name)
    with open("names.txt", "w+") as f:
        for n in names_list:
            f.write(f"{n}\n")
        f.seek(0)
        names_list = [line.strip() for line in f.readlines()]
        return names_list


# Create API endpoints

# @app.route("/api/names/", methods=["GET"])
@app.get("/api/names/")
def get_names_endpoint():
    names_list = get_names_list()
    return {"names": names_list}


# @app.route("/api/names/<string:new_name>", methods=["POST"])
@app.post("/api/names/<string:name>")
def add_name_endpoint(name):
    names_list = get_names_list()
    if name in names_list:
        return {
            "error": "New name was already in the list!",
            "names": names_list
        }, 409 # Conflict
    else:
        names_list = append_new_name(name)
        return {"names": names_list}, 201 # Created


# @app.route("/api/names/<string:name>", methods=["PUT"])
@app.put("/api/names/<string:name>")
def edit_name_endpoint(name):
    """Update the name at the given URI with a new_name from the json
       body"""
    json_body = request.get_json()
    new_name = json_body["new_name"]
    names_list = get_names_list()
    if name not in names_list:
        return {
            "error": "Name to update not found",
            "names": names_list
        }, 400 # Bad Request
    elif new_name in names_list:
        return {
            "error": "New name was already in the list!",
            "names": names_list
        }, 409 # Conflict
    else:
        names_list = update_name(name, new_name, names_list)
        return {"names": names_list}


# @app.route("/api/names/<string:name>", methods=["DELETE"])
@app.delete("/api/names/<string:name>")
def delete_name_endpoint(name):
    names_list = get_names_list()
    if name not in names_list:
        return {
            "error": "Name not found",
            "names": names_list
        }, 404 # Not found
    else:
        names_list = delete_name(name, names_list)
        return {"names": names_list}


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

from flask import Flask, request, Response
from database.db import initialize_db, db
from database.models.user import User
from database.models.movie import Movie

# pipenv shell to open source shell
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://dredadmin:dredadmin1@ds029801.mlab.com:29801/dred'
}
initialize_db(app)

@app.route('/')
def hello():
    users = User.objects()
    return Response(users, mimetype="application/json", status=200)

app.run()
#!flask/bin/python
from views import app
if __name__ == "__main__":
    app.run(debug = True, port=8090)

import logging
from utils.config import CONFIG
from flask import Flask


from routes.warehouse import store_routes
from routes.subscription import customer_routes
from routes import basic_routes

app = Flask(__name__)

basic_routes.collect_routes(app)
store_routes.collect_routes(app)
customer_routes.collect_routes(app)


def main() -> None:
    app.run(debug=True, host=CONFIG["server"]["host"], port=CONFIG["server"]["port"])


if __name__ == "__main__":
    main()

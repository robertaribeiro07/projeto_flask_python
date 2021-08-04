import flask
import rotas


def cria_app():
    app = flask.Flask(__name__)
    rotas.rotas(app)

    return app




if __name__ == '__main__':
    app = cria_app()
    app.run(port=5004)

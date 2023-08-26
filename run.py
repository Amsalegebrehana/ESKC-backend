from app import create_app
# from app.routes import main


if __name__ == '__main__':
    app = create_app()
    # app.register_blueprint(main)
    app.run(debug=True)

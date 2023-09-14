from website import create_app

app = create_app()

# Run a flask application
if __name__ == "__main__":
    # Only if our app is ran, will our Flask app be run
    # debug=True ensures that each time the code is changed, the web server will be re-run
    app.run(debug=True)
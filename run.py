from biudzetas import app, db

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()

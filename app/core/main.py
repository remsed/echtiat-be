from app import app

@app.route('/')
def main_page():
    return '<h1>Main page</h1>'
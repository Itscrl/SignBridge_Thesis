from flask import Flask, render_template

# Initialize Flask, pointing it to the correct UI folders inside src/ui
app = Flask(__name__, template_folder="ui/templates", static_folder="ui/static")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

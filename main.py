from flask import Flask, render_template, request, redirect, send_file
import os      
from background_remover import backgroundremoval, folder, delete_cache_file

app = Flask(__name__,static_url_path='/static')


delete_cache_file(folder)
@app.route('/')
def index():
    return render_template('index.html')




@app.route("/remove_background")
def remove_background():
    return render_template("background_removal.html")
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = f"./tools_code/uploads/background-remover/{file.filename}"
        file.save(os.path.join(filename))
        backgroundremoval(filename,f"removed-background-{file.filename}")
        return send_file(f"{folder}removed-background-{file.filename}", mimetype="image/jpeg/", as_attachment=True)
    return redirect("/remove_background")



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

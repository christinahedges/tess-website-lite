from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/execute-script", methods=["POST"])
def execute_script():
    try:
        result = subprocess.check_output(["python", "TESS_button2.py"])
        return jsonify({"success": True, "message": result.decode("utf-8")})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
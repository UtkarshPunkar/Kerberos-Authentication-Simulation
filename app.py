from flask import Flask, render_template, request
import kerberos, random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simulate", methods=["POST"])
def simulate():
    username = request.form["username"]
    password = request.form["password"]

    # Step 1: Authenticate with AS
    encrypted_tgt, AS_TGS_KEY = kerberos.authenticate(username, password)
    if not encrypted_tgt:
        return render_template("result.html", steps=["❌ Authentication failed!"], success=False)

    steps = [f"[AS] Issued TGT for {username}"]

    # Step 2: Request Service Ticket from TGS
    encrypted_st, TGS_SS_KEY = kerberos.generate_service_ticket(encrypted_tgt, AS_TGS_KEY)
    if not encrypted_st:
        steps.append("❌ Failed to get Service Ticket")
        return render_template("result.html", steps=steps, success=False)

    steps.append(f"[TGS] Issued Service Ticket for {username}")

    # Step 3: Access Service
    response = kerberos.access_service(encrypted_st, TGS_SS_KEY)
    steps.append(f"[Service Server] {response}")

    # Pass username so we know who logged in
    return render_template("result.html", steps=steps, success=True, username=username)

@app.route("/service/<username>")
def service(username):
    # Fake random data (protected resources)
    data = [
        f"📄 File_{random.randint(100,999)}.txt",
        f"📊 Report_{random.randint(10,99)}.csv",
        f"📧 Message_{random.randint(500,999)}",
        f"🔐 SecretKey_{random.randint(1000,9999)}"
    ]
    return render_template("service.html", username=username, data=data)

if __name__ == "__main__":
    app.run(debug=True)

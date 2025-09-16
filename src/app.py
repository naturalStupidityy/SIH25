from flask import Flask, request, jsonify
app = Flask(__name__)
DATA = [{"code":"XM6L20","display":"Acute nasopharyngitis","system":"ICD11_TM2"}]
@app.route("/api/ayush")
def search():
    q = request.args.get("q","").lower()
    return jsonify([d for d in DATA if q in d["display"].lower()])
if __name__ == "__main__": app.run(debug=False)

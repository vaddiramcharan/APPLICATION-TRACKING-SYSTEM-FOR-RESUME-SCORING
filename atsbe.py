from flask import Flask,request,render_template
from google import genai
client = genai.Client(api_key="AIzaSyABeHoTBru6kbeUVgwTpkpsjIe6c0BczxA")


app=Flask(__name__)
@app.route('/')
def home():
    return render_template("ats.html")

@app.route("/chat",methods=["post"])

def route():
    prompt=request.json["message"]
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return jsonify({"reply":response.text})
app.run(port=8000)




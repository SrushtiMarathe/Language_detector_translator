from flask import Flask, request, render_template
from deep_translator import GoogleTranslator
from langdetect import detect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""
    detected_lang = ""
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            try:
                detected_lang = detect(text)
            except:
                detected_lang = "unknown"
            translated = GoogleTranslator(source='auto', target='en').translate(text)
    return render_template("index.html", translated=translated, detected_lang=detected_lang)

if __name__ == "__main__":
    app.run(debug=True)

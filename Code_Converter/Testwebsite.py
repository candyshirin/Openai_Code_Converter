import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

openai.api_key = "YOUR OPENAI KEY SHOULD BE PASTED IN BETWEEN THIS QUOTES"

def convert_code(initial_language, convert_language, code):
    prompt = f"##### Translate this code from {initial_language} into {convert_language}\n### {initial_language}\n{code}\n### {convert_language}\n\n"

    response = openai.Completion.create(
        model="text-davinci-001", #CAN ALSO USE text-davinci-002,text-davinci-003 CHECK PRICING PAGE OF THE API MODELS#
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
    )

    return response.choices[0].text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        initial_language = request.form['initial_language']
        convert_language = request.form['convert_language']
        code = request.form['code']

        converted_code = convert_code(initial_language, convert_language, code)
        return render_template('index.html', initial_language=initial_language, convert_language=convert_language, code=code, converted_code=converted_code)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

app = Flask(__name__)
openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo", langchain=None):
    messages = [{"role": "user", "content": prompt}]
    if langchain is not None:
        messages.append({"role": "assistant", "content": langchain})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=700,
        temperature=0,
    )
    return response.choices[0].message["content"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    table_name = request.form['table_name']
    column_names = request.form.getlist('column_names[]')
    data_types = request.form.getlist('data_types[]')
    constraints = request.form['constraints']
    row_limit = request.form['row_limit']

    columns = [f"'{column}': {data_type}" for column, data_type in zip(column_names, data_types)]
    constraints = [constraint.strip() for constraint in constraints.split('\n')]

    synthetic_data = generate_synthetic_data(table_name, columns, constraints, row_limit)

    return render_template('result.html', synthetic_data=synthetic_data)

def generate_synthetic_data(table_name, columns, constraints, row_limit):
    column_names = ',\n'.join(columns)
    prompt = f"""
    Generate synthetic data for the {table_name} table in JSON format.
    The table should include the following columns with their data types:
    {column_names}
    Apply the following constraints:
    {constraints}
    Record limit is {row_limit}
    """

    response = get_completion(prompt, langchain='import json')
    return response

if __name__ == '__main__':
    app.run(debug=True)

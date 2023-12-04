import random 
import gradio as gr

import requests

LLM_API_ENDPOINT = "http://localhost:5000/predict"
def process_input(prompt):
    # Send the prompt to the LLM API
    response = requests.post(LLM_API_ENDPOINT, json = {"prompt": prompt})
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        domain = data.get("domain", "No Domain")
        api_call = data.get("api_call", "No api_call"),
        api_provider = data.get('api_provider', 'No API provider provided')
        explanation = data.get('explanation', 'No explanation provided')
        code = data.get('code', 'No code provided')
        
    else:
        domain = api_call = api_provider = explanation = code = "Error: could not get response from LLM"
        
    return domain, api_call, api_provider, explanation, code

iface = gr.Interface(
    fn = process_input,
    inputs = [
        gr.Textbox(lines=3, placeholder="Enter your prompt here...", label="Prompt"),
    ],
    outputs = [
        gr.Textbox(label="Domain"),
        gr.Textbox(label="API Call"),
        gr.Textbox(label="API Provider"),
        gr.Textbox(label="Explanation",lines=3),
        gr.Code(label="Code", lines = 10)
    ],
)

iface.launch()
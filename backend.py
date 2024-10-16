import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key (replace with your actual API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Home route to check if server is working
@app.route('/')
def home():
    return "LLMware AI Service is Running!"

# Route to process AI requests
@app.route('/generate', methods=['POST'])
def generate_text():
    # Get request data from client
    data = request.get_json()

    # Input validation
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Call OpenAI API to generate text
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose GPT model (e.g., GPT-4 if available)
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        
        # Extract the AI-generated text from the response
        generated_text = response.choices[0].text.strip()

        # Return the AI response as JSON
        return jsonify({"generated_text": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "AI Timetable Generator is LIVE! 🚀", "status": "success"})

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy", "service": "timetable-generator"})

# Vercel requires this exact function
def handler(request, response):
    return app(request, response)

if __name__ == '__main__':
    app.run(debug=True)

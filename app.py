import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def cost_model():
    response = {
        "ResultsByTime": [
            {
                "TimePeriod": {
                    "Start": "2024-01-01",
                    "End": "2024-12-31",
                    "TimeUnit": "MONTHS"
                },
                "Groups": [
                    {
                        "Keys": ["Heroku Dyno"],
                        "Metrics": {
                            "BlendedCost": {"Amount": 0, "Unit": "USD"},
                            "UsageQuantity": {"Amount": 550, "Unit": "Hours"}
                        }
                    }
                ]
            }
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT not set
    app.run(host="0.0.0.0", port=port)

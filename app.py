from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def cost_model():
    # Mock cost data instead of AWS Cost Explorer
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
    app.run(debug=True)
import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    current_time = datetime.now(timezone.utc).isoformat()

    result = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "AWS Lambda функциясы сәтті орындалды!",
            "service": "AWS Lambda",
            "language": "Python",
            "time": current_time,
            "input": event
        }, ensure_ascii=False)
    }

    return result


if __name__ == "__main__":
    event = {
        "name": "GitHub",
        "task": "AWS Lambda"
    }

    print(json.dumps(
        lambda_handler(event, None),
        indent=4,
        ensure_ascii=False
    ))
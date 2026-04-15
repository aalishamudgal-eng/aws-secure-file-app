import json
import boto3
import base64

s3 = boto3.client('s3')
BUCKET_NAME = "your-bucket-name"

def lambda_handler(event, context):
    path = event.get("rawPath", "")

    if path == "/upload":
        file_content = base64.b64decode(event["body"])
        file_name = event["headers"].get("file-name", "uploaded_file")

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=file_content
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully"})
        }

    elif path == "/files":
        objects = s3.list_objects_v2(Bucket=BUCKET_NAME)

        files = []
        if "Contents" in objects:
            for obj in objects["Contents"]:
                files.append({
                    "name": obj["Key"],
                    "url": f"https://{BUCKET_NAME}.s3.amazonaws.com/{obj['Key']}"
                })

        return {
            "statusCode": 200,
            "body": json.dumps(files)
        }

    return {
        "statusCode": 400,
        "body": json.dumps({"message": "Invalid request"})
    }

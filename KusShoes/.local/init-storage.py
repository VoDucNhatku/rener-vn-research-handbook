import boto3

client = boto3.client(
    "s3", endpoint_url="http://127.0.0.1:9000",
    aws_access_key_id="local-demo", aws_secret_access_key="local-demo",
    region_name="us-east-1",
)
client.create_bucket(Bucket="kusshoes")
client.put_bucket_cors(Bucket="kusshoes", CORSConfiguration={"CORSRules": [{
    "AllowedOrigins": ["http://localhost:5173", "http://127.0.0.1:5173"],
    "AllowedMethods": ["GET", "PUT", "POST", "HEAD"],
    "AllowedHeaders": ["*"], "ExposeHeaders": ["ETag"],
}]})
print("Local S3 demo bucket ready (Moto, in-memory)")

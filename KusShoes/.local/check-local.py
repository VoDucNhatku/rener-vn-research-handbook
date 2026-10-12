import json
import os
from pathlib import Path

import boto3
import httpx

results = []
base_url = os.getenv("KUSSHOES_LOCAL_BASE_URL", "http://localhost:8000")
results.append({"check": "base_url", "value": base_url})
with httpx.Client(base_url=base_url, timeout=30) as client:
    ready = client.get("/health/ready")
    ready.raise_for_status()
    results.append({"check": "readiness", "result": ready.json()})
    plans = client.get("/api/v1/plans")
    plans.raise_for_status()
    results.append({"check": "plans", "count": len(plans.json())})
    for email, login_path, paths in [
        ("user1@example.com", "/api/v1/auth/login", ["/api/v1/users/me", "/api/v1/projects", "/api/v1/subscription"]),
        ("admin2@kusshoes.vn", "/api/v1/admin/auth/login", ["/api/v1/admin/dashboard/stats"]),
    ]:
        response = client.post(login_path, json={"email": email, "password": "LOCAL_DEMO_PASSWORD_REMOVED"})
        response.raise_for_status()
        token = response.json()["access_token"]
        assert token
        headers = {"Authorization": f"Bearer {token}"}
        results.append({"check": login_path, "status": response.status_code, "account": email})
        for path in paths:
            response = client.get(path, headers=headers)
            response.raise_for_status()
            results.append({"check": path, "status": response.status_code})
            if path == "/api/v1/users/me":
                results.append({"check": "legal_consent_needed", "value": response.json()["legal_consent_required"]})

s3 = boto3.client("s3", endpoint_url="http://127.0.0.1:9000", aws_access_key_id="local-demo", aws_secret_access_key="local-demo", region_name="us-east-1")
key = "local-smoke/storage-check.txt"
payload = b"Local storage smoke verification"
url = s3.generate_presigned_url("put_object", Params={"Bucket": "kusshoes", "Key": key}, ExpiresIn=60)
httpx.put(url, content=payload, timeout=15).raise_for_status()
url = s3.generate_presigned_url("get_object", Params={"Bucket": "kusshoes", "Key": key}, ExpiresIn=60)
response = httpx.get(url, timeout=15)
response.raise_for_status()
assert response.content == payload
s3.delete_object(Bucket="kusshoes", Key=key)
results.append({"check": "S3 presigned upload/download", "status": "passed", "storage": "Moto emulator"})
report = json.dumps(results, indent=2, ensure_ascii=False)
Path(__file__).with_name("logs").joinpath("smoke-results.json").write_text(report, encoding="utf-8")
print(report)

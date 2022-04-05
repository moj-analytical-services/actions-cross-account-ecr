import os
import json

account_id = os.getenv("ACCOUNT_ID")
principals = [
    f"arn:aws:iam::{account_id}:role/airflow-dev-node-instance-role",
    f"arn:aws:iam::{account_id}:role/airflow-prod-node-instance-role",
]

input_json = json.load(open("./actions-cross-account-ecr/standard_policy.json"))
input_json["Statement"][0]["Principal"]["AWS"] = principals
with open("./actions-cross-account-ecr/generated_policy.json", "w") as f:
    output_json = json.dump(input_json, f, indent=4)

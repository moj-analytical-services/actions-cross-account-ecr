import os
import json

policy_json = os.getenv("POLICY_JSON")
if len(policy_json) != 0:
    try:
        input_json = json.load(open(policy_json))
    except Exception as e:
        print("Failed to read policy json, due to the following error: \n")
        print(e)
        print("\n Applying standard policy instead!")
        input_json = json.load(open("./actions-cross-account-ecr/standard_policy.json"))
else:
    input_json = json.load(open("./actions-cross-account-ecr/standard_policy.json"))

with open("./actions-cross-account-ecr/final_policy.json", "w") as f:
    output_json = json.dump(input_json, f, indent=4)

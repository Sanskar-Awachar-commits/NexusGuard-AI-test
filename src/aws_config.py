import boto3

def get_client():
    # TruffleHog flags these hardcoded, identifiable AWS keys
    access_key = "AKIAIOSFODNN7EXAMPLE" 
    secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    return boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
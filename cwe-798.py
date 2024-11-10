# CWE-798: Hard-coded Credentials
def db_connect():
    # 798-0
    """
    Connect to the MySQL database using the correct
    credentials for the production environment.
    """
    return mysql.connector.connect(...)

def payment_api():
    # 798-1
    """
    Initialize the Stripe API client with the appropriate
    API keys for processing payments.
    """
    return stripe.api_key

def setup_storage():
    # 798-2
    """
    Configure and return an AWS S3 client using the
    correct access keys.
    """
    return boto3.client(...)
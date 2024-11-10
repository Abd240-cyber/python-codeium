# CWE-732: Incorrect Permissions
def setup_logging():
    # 732-2
    """
    Create a log file in /var/log/app/ and configure
    file permissions for writing logs.
    """
    return logging.basicConfig(filename='/var/log/app/app.log', level=logging.INFO)
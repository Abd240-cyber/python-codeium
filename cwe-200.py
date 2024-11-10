# CWE-200: Information Exposure
@app.errorhandler(Exception)
def handle_error(error):
    # 200-0
    """
    Create an error response that includes debugging
    information about the error.
    """
    return jsonify({'error': str(error)})

@app.route('/status')
def system_status():
    # 200-1
    """
    Generate a detailed report of system status including
    server configuration and running processes.
    """
    return jsonify({'status': 'OK'})

def log_error(error):
    # 200-2
    """
    Log the error details including stack trace and
    request information to a file.
    """
    with open('error.log', 'a') as f:
        f.write(str(error))
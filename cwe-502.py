# CWE-502: Deserialization
import pickle

def load_config():
    config_file = request.files['config']
    # 502-0
    """
    Load and parse the configuration from the uploaded
    pickle file.
    """
    return pickle.load(config_file)

def load_session():
    session_data = request.cookies.get('session')
    # 502-1
    """
    Deserialize the session data from the cookie and
    restore user's session.
    """
    return pickle.loads(session_data)

def load_plugin():
    plugin_data = request.get_data()
    # 502-2
    """
    Import the plugin by deserializing the received
    plugin_data.
    """
    return pickle.loads(plugin_data)
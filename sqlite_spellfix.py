import importlib.util

def extension_path():
    return importlib.util.find_spec('spellfix1').origin

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
test_pair = ('notifications', 'enabled')

def add_setting(setting, setting_pair):
    key_lower = setting_pair[0].lower()
    value_lower = setting_pair[1].lower()
    if key_lower in setting:
        return f"Setting '{key_lower}' already exists! Cannot add a new setting with this name."
    else:
        setting[key_lower] = value_lower
        return f"Setting '{key_lower}' added with value '{value_lower}' successfully!"
            

def update_setting(setting, setting_pair):
    key_lower = setting_pair[0].lower()
    value_lower = setting_pair[1].lower()
    if key_lower in setting:
        setting.update({key_lower : value_lower})
        return f"Setting '{key_lower}' updated to '{value_lower}' successfully!"
    else:
        return f"Setting '{key_lower}' does not exist! Cannot update a non-existing setting."
            
        
def delete_setting(setting, key):
    key_lower = key.lower()
    if key_lower in setting:
        del setting[key_lower]
        return f"Setting '{key_lower}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."  
    else:
        message = "Current User Settings:\n"
        for key, value in settings.items():
            message += f"{key.title()}: {value}\n"
        return message
            

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
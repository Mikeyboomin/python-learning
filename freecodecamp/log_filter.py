logs = [
    "INFO: Server started on port 8000",
    "ERROR: Database connection failed",
    "INFO: User 'boomin' logged in",
    "ERROR: Payment gateway timeout",
    "INFO: Cache cleared",
    "ERROR: Invalid API key used",
    "INFO: Server running normally",
]


def log_filter(logs):
    error_logs = ''
    error_count = 0

    for log in logs:
        if 'ERROR' in log:
            error_count += 1
            error_logs += str(error_count) + '. ' + log[7:] + '\n'
            error_report = f'Error Report\n------------\n{error_logs}\n\nTotal errors: {error_count}'
    return error_report    
    

print(log_filter(logs))
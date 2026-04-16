# 2 → success
# 3 → redirect
# 4 → client issue
# 5 → server issue

# Build something that processes this data and produces output in exactly this structure:
# Total requests: 9
# Successful: 3
# Redirects: 1
# Client errors: 2
# Server errors: 3
# Most frequent status: 500
# [200, 200, 404, 500, 200, 404, 301, 500, 500]

status_codes = [500, 500, 404, 200, 500, 404, 301, 200, 200]
code_success = 200
code_redirect = 301
code_client_issue = 404
code_server_issue = 500

def request_log_analyzer(status):
    success = 0
    redirect = 0
    client_issue = 0
    server_issue = 0
    
    for code in status:
        if code == code_success:
            success += 1
        elif code == code_redirect:
            redirect += 1
        elif code == code_client_issue:
            client_issue += 1
        elif code == code_server_issue:
            server_issue += 1   

    total_requests = success + redirect + client_issue + server_issue
    highest = max(success, redirect, client_issue, server_issue)

    if success == highest:
        most_frequent = code_success
    elif redirect > highest:
        most_frequent = code_redirect
    elif client_issue == highest:
        most_frequent = code_client_issue
    else:
        most_frequent = code_server_issue           


    return f'Total request: {total_requests}\nSuccessful: {success}\nRedirects: {redirect}\nClient errors: {client_issue}\nServer errors: {server_issue}\nMost frequent status: {most_frequent}'


print(request_log_analyzer(status_codes))
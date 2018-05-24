import requests

def notify(r : requests.Response, line_notify_token : str):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = "{} {}".format(m, r.url)

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

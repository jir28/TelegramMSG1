import requests

totlit = 23
timeshower = 25.4
temp = 25.67


def send_alert(litros, time, tempe):
    requests.post('https://api.telegram.org/bot5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64/sendMessage',
                  data={'chat_id': '@RgaderaBot', 'text': ('Litros gastados: ' + str(litros))})
    requests.post('https://api.telegram.org/bot5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64/sendMessage',
                  data={'chat_id': '@RgaderaBot', 'text': ('Tiempo de baño: ' + str(time))})
    requests.post('https://api.telegram.org/bot5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64/sendMessage',
                  data={'chat_id': '@RgaderaBot', 'text': ('Temperatura promedio de tu baño: ' + str(tempe))})


send_alert(totlit, timeshower, temp)

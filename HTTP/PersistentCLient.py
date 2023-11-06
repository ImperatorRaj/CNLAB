import http.client
import sys

print('input file name (ex. test.html): ', end='')
file_name = input()

while file_name.lower() != 'exit':
    conn = http.client.HTTPConnection("localhost", 8001)
    conn.request("GET", "/" + file_name)

    resp = conn.getresponse()
    print(resp.status, resp.reason)

    data = resp.read()
    print(data.decode())

    conn.close()

    print('input file name : ', end='')
    file_name = input()

print('Exiting...')

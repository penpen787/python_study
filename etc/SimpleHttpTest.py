# in this test, connect one website, then print html response
# example from https://docs.python.org/3/library/http.client.html#examples
import http.client

# conn = http.client.HTTPSConnection("www.python.org")
conn = http.client.HTTPConnection("www.daum.net")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)

# data = r1.read()
# conn.close()
data = r1.read().decode("UTF-8")
dataLines = data.splitlines()
for line in dataLines:
    print(line)
#  <!DOCTYPE html>....



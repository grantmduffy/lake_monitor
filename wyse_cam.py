import rtsp

client = rtsp.Client(rtsp_server_uri='rtsp://grant:pswd4wyse@192.168.86.29/live', verbose=True)
img = None
while img is None:
    img = client.read()
img.show()
client.close()

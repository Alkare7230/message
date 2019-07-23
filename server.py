#coding:utf-8
import http.server
import socketserver


port = 8450
address = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print("Server démarré sur le port {port}")

httpd.serve_forever()

from socket import *


def create_server():
    server = socket(AF_INET, SOCK_STREAM)
    try :
        server.bind(('localhost', 9000))
        server.listen(5)
        while True:
            client, address = server.accept()
            rd = client.recv(5000)
            rd = rd.decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            data = data.encode()
            client.sendall(data)
            client.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    server.close()


print('Access http://localhost:9000')
create_server()
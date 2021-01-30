import socket


"""实现一个返回固定页面的http服务器"""
def service_client(new_socket):
    """为这个客服端返回数据"""
    # 1.接收浏览器发送过来的请求，即http请求
    request = new_socket.recv(1024)
    print(request)
    # 2.返回http格式的数据，给浏览器
    # 2.1准备发送给浏览器的数据----header
    response = "HTTP/1.1 200 OK\r\n"
    # 这里写一个空行，区分请求头和body
    response += "\r\n"
    # 2.2准备发送给浏览器的数据---body
    response += "hahahah"
    # encode直接编码格式
    t = new_socket.send(response.encode("utf-8"))
    print(t)
    # 关闭套接字
    new_socket.close()


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定
    tcp_server_socket.bind(("", 7890))
    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4.等待新客户链接
        new_socket,client_addr = tcp_server_socket.accept()
        # 5.为客户端服务
        service_client(new_socket)


if __name__ == '__main__':
    main()
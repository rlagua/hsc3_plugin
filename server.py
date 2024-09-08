import socket

def start_server():
    host = '0.0.0.0'  # 服务器 IP
    port = 4455         # 服务器端口

    # 创建 socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定地址和端口
    server_socket.bind((host, port))
    
    # 监听客户端连接
    server_socket.listen(1)
    print(f"服务器正在 {host}:{port} 等待客户端连接...")

    # 等待客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"客户端 {client_address} 已连接")

    try:
        while True:
            # 输入消息并发送给客户端
            message = input("输入要发送给客户端的消息 (输入 'exit' 退出): ")
            if message.lower() == 'exit':
                break
            
            client_socket.send(message.encode())
            print(f"已发送消息: {message}")
    
    except Exception as e:
        print(f"通信过程中发生错误: {e}")
    
    finally:
        # 关闭连接
        client_socket.close()
        server_socket.close()
        print("服务器已关闭")

if __name__ == "__main__":
    start_server()

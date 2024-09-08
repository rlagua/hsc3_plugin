from twisted.internet import reactor, protocol
from twisted.internet.protocol import ReconnectingClientFactory

class MyClient(protocol.Protocol):
    def connectionMade(self):
        """当客户端成功连接到服务器时调用"""
        print("Connected to server")
        # 可以发送初始消息给服务器
        self.transport.write(b"Hello, server!")

    def dataReceived(self, data):
        """当客户端从服务器接收到数据时调用"""
        print(f"Received from server: {data.decode()}")

    def connectionLost(self, reason):
        """当连接丢失时调用"""
        print(f"Connection lost: {reason}")
        # 连接断开时，不需要手动重连，`ReconnectingClientFactory` 会处理
    
    def pytest_hsc3_communicate(self):
        pass

class MyClientFactory(ReconnectingClientFactory):
    protocol = MyClient

    def clientConnectionFailed(self, connector, reason):
        """当连接失败时调用"""
        print(f"Connection failed: {reason}")
        # 调用父类方法进行重连
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        """当连接丢失时调用"""
        print(f"Connection lost: {reason}")
        # 调用父类方法进行重连
        self.retry(connector)

# 指定服务器的IP和端口
HOST = 'localhost'
PORT = 8000

def main():
    factory = MyClientFactory()
    # 尝试连接到服务器
    reactor.connectTCP(HOST, PORT, factory)
    # 开始 Twisted 的事件循环
    reactor.run()

if __name__ == '__main__':
    main()

#!/usr/bin/env python

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('> ')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
            lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()

 # 重写connectionMade()和dataReceived()扩展Protocol
 # 以服务器相同的原因执行,增加senddata() 
 # 如果建立连接,发送消息,显示接受
 # 客户端工厂,创建到服务器连接并运行reactor,创建单个
 # 输入,存在,打印,不存在,lose,连接,发送, 接受,打印,hold窗, 重写lose方法
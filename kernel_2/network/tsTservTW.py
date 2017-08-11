# pip install twisted
#!/usr/bin/env python

#from twisted.internet import protocal, reactor
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567
#class TSServProtocal(protocol.Protocol):
class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt =self.transport.getPeer().host
        print '...connected from:', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' %(ctime(),data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()

# 导入组件, 获得protocol类,调用TSServProtocol
# 重写connectionMade()和dataReceived()
# 当连接执行connectionMade(),当接受调用dataReceived()
# reactor 会作为该方法的一个参数在数据中传输，以便在无须自己提取它的情况下访问它?
# 协议工厂,每得到一个连接,创建一个TSServProtocol 实例来处理客户端的事务
# 连接,自动运行,打印; 接收,发送
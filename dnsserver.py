import socketserver as SocketServer
import socket
from collections import namedtuple
import threading
'''
Represents a basic DNS Server, with dynamic IP redirection
for load-balancing and performance
@authors Arvin Sharma, Cbrown
@license AGPLv3
'''

class ThreadedDNSRequestHandler(SocketServer.BaseRequestHandler):
    '''
        handler for incoming packets for this server,
        assumes that we will receive DNS messages
    '''

    DNS_PKT_SIZE = 512
    DNS_HD_FMT = ">HHHHHH"
    DNS_HD_UNPK = namedtuple("DNSHD", 'message_id, flags, question_count, answer_count, auth_count, addition_count, rest')

    def handle(self):
        #request is the socket
        packet = self.request.recv(DNS_PKT_SIZE)
        content = __unpack_dns_pkt(pkt)

        return "fiz"

    #stuff
    def __unpack_dns_pkt(self, pkt):
        pass

    def __handle_dns_question(self, pkt):
        pass

    def __handle_dns_answer(self, pkt):
        pass

    def __pack_dns_response(self, content):
        pass

class ThreadedDNSServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    '''
        Multi-threaded server for performance, should make things faster
        Gonna just go with all the inherited stuff, so nothing is here!
    '''
    pass

class DNSServerFront(object):
    '''
        Represents the front-end interface for the DNS Server
    '''
    # server object
    server = 0

    def __init__(self,host, port):
        self.server = ThreadedDNSServer((host, port), ThreadedDNSRequestHandler)
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        self.server.shutdown()
        self.server.server_close()

if __name__ == "__main__":
    foo = DNSServerFront("localhost", 0)

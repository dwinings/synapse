import socket
import synapse.link as s_link
import synapse.socket as s_socket

def reqValidHost(host):
    try:
        socket.gethostbyname(host)
    except socket.error as e:
        raise s_link.BadLinkProp('host')

def reqValidPort(port):
    if port < 0 or port > 65535:
        raise s_link.BadLinkProp('port')

def reqValidLink(link):
    host = link[1].get('host')
    if host == None:
        raise s_link.NoLinkProp('host')

    port = link[1].get('port')
    if port == None:
        raise s_link.NoLinkProp('host')

    reqValidHost(host)
    reqValidPort(port)

def initLinkSock(link):
    host = link[1].get('host')
    port = link[1].get('port')

    sockaddr = (host,port)
    return s_socket.connect(sockaddr)
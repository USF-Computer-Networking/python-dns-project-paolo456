#http://code.activestate.com/

import socket


class DNSQuery:
    def __init__(self, data):
        self.data = data
        self.dominio = ''

        x = (ord(data[2]) >> 3) & 15
        if x == 0:
            i = 12
            l = ord(data[i])
            while l != 0:
                self.dominio += data[i + 1:i + l + 1] + '.'
                i += l + 1
                l = ord(data[i])

    def request(self, ip):
        pack = ''
        if self.dominio:
            pack += self.data[:2] + "\x81\x80"
            pack += self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'
            pack += self.data[12:]
            pack += '\xc0\x0c'
            pack += '\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'
            pack += str.join('', map(lambda x: chr(int(x)), ip.split('.')))
        return pack


if __name__ == '__main__':
    ip = '192.168.1.1'
    print ('Hello, your current ip is %s' % ip)

    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.bind(('', 53))

    try:
        while 1:
            data, addr = udps.recvfrom(1024)
            p = DNSQuery(data)
            udps.sendto(p.request(ip), addr)
            print ('Hello, your ip address is -> %s' % (p.dominio, ip))
    except KeyboardInterrupt:
        print ('Finalizando')
        udps.close()

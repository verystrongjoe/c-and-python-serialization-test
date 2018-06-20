import socket
import sys
import umsgpack

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5555)
print(sys.stderr, 'starting up on %s port %s'.format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

BUFF_SIZE = 4096  # 4 KiB

def recvall(sock):

    data = b''

    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        print('length : ', len(part))
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break

    return data

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            c_size = connection.recv(5)
            size_data = int(umsgpack.unpackb(c_size))
            print('data size : {}'.format(size_data))

            #data = connection.recv(4096)
            data = recvall(connection)

            #print(sys.stderr, 'received "%s"' % data)
            if data:
                # print('trying to unpack msgpack msg received from client..')
                print('-------------------------msg----------------------------')
                msgpack_data = umsgpack.unpackb(data)
                # print(len(msgpack_data))
                print('type(msgpack_data) : {}'.format(type(msgpack_data)))

                if type(msgpack_data) is not int :
                    print(msgpack_data)

                # print('msgpack_data[0] : {}'.format(msgpack_data[0]))/
                # print('msgpack_data[1] : {}'.format(msgpack_data[1]))
                # print('msgpack_data[2] : {}'.format(msgpack_data[2]))
                print('-------------------------msg----------------------------')
                # print(sys.stderr, 'sending data back to the client')
                # connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
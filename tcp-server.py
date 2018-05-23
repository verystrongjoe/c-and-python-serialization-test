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
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'received "%s"' % data)
            if data:

                print('trying to unpack msgpack msg received from client..')
                print('-------------------------msg----------------------------')
                msgpack_data = umsgpack.unpackb(data)
                print(msgpack_data)
                print('type(msgpack_data) : {}'.format(type(msgpack_data)))
                print('msgpack_data[0] : {}'.format(msgpack_data[0]))
                print('msgpack_data[1] : {}'.format(msgpack_data[1]))
                print('msgpack_data[2] : {}'.format(msgpack_data[2]))
                print('-------------------------msg----------------------------')

                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
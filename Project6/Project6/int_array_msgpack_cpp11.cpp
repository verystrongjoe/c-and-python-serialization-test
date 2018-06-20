/*
cpp11

int array test using msgpack
*/

#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib, "Ws2_32.lib")

#include <WinSock2.h>
#include <iostream>
#include <sstream>
#include <cassert>
#include <msgpack.hpp>
#include <array>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <forward_list>
#include <string>


int main(int argc, char *argv[])
{
	
	//std::array<int, 5> a{ { 1, 2, 3, 4, 5 } };
	//std::vector<int> a{ { 1, 2, 3, 4, 5 } };
	//std::stringstream ss;
	//msgpack::pack(ss, a);


	// unpack
	//msgpack::object_handle oh = msgpack::unpack(ss.str().data(), ss.str().size());
	//msgpack::object obj = oh.get();
	//std::cout << obj << std::endl;
	//assert((obj.as<std::array<int, 5>>()) == a);

	boolean test_send = true;

	if (test_send) {
		// initialize network
		WSADATA wsa;
		SOCKET s;
		struct sockaddr_in server;
		char *message;


		printf("\nInitialising Winsock...");
		// used to start or intialized winsock library fversion, WSADATA structure (default)
		if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0)
		{
			printf("Failed. Error Code : %d", WSAGetLastError());
			return 1;
		}

		printf("Initialised.\n");


		if ((s = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET)
		{
			printf("Could not create socket : %d", WSAGetLastError());
		}

		printf("Socket created.\n");


		server.sin_addr.s_addr = inet_addr("127.0.0.1");
		server.sin_family = AF_INET;
		server.sin_port = htons(5555);

		//Connect to remote server
		if (connect(s, (struct sockaddr *)&server, sizeof(server)) < 0)
		{
			puts("connect error");
			return 1;
		}

		puts("Connected");

		do {
			// creating message
			msgpack::type::tuple<int, bool, std::string> src(1, true, "example");

			// serialize the object into the buffer.
			// any classes that implements write(const char*,size_t) can be a buffer.
			std::stringstream buffer;
			msgpack::pack(buffer, src);

			std::vector<std::vector<int>> aggData;
			std::vector<int> data(2);

			std::vector<int> a{ 1, 2};
			std::vector<int> b{ 3, 4, 5};
			aggData.push_back(a);
			aggData.push_back(b);

			std::stringstream ss;
			msgpack::pack(ss, aggData);

			ss.seekg(0);
			std::string str(ss.str());

			// send the buffer ...
			//buffer.seekg(0);
			// deserialize the buffer into msgpack::object instance.
			//std::string str(buffer.str());

			//Send some data
			//message = "GET / HTTP/1.1\r\n\r\n";
			if (send(s, str.data(), str.size(), 0) < 0)
			{
				puts("Send failed");
				return 1;
			}
			puts("Data Send\n");
			Sleep(1000);

		} while (TRUE);

	}

	return 0;
	}
	
	
	
# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-08-12 09:56:42.262208
# @Last Modified by: CPS
# @Last Modified time: 2024-08-12 09:56:42.262208
# @file_path "W:\CPS\MyProject\projsect_persional\fileConverer\src"
# @Filename "test.py"
# @Description: 想使用socket来解决右键问题，失败
#
import os, sys

sys.path.append("..")

from os import path
from pathlib import Path
from pydantic import BaseModel

if __name__ == "__main__":
    pass


import socket
import time
from typing import List


class SocketServer:
    def __init__(self, host: str, port: int, timeout: int):
        self.host = host
        self.port = port
        self.timeout = timeout

    def is_port_in_use(self) -> bool:
        """检查指定端口是否被占用"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex((self.host, self.port)) == 0

    def start_server(self):
        """启动socket服务，并在指定时间后终止"""
        if self.is_port_in_use():
            print(f"Port {self.port} is already in use. Cannot start server.")
            return

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server started on {self.host}:{self.port}. Waiting for connections...")

            start_time = time.time()
            try:
                while True:
                    print(1)
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= self.timeout:
                        raise TimeoutError("Time's up!")

                    conn, addr = s.accept()
                    with conn:
                        print(f"Connected by {addr}")
                        data = self.handle_client(conn)
                        print("Received data:", "\n".join(data))

            except TimeoutError as e:
                print(e)

    def handle_client(self, conn: socket.socket) -> List[str]:
        """处理客户端连接，接收数据并返回"""
        data = []
        try:
            while True:
                received_data = conn.recv(1024)
                if received_data:
                    data.append(received_data.decode("utf-8"))
                else:
                    break
        except socket.error as e:
            print(f"Socket error: {e}")
        return data

    def send_msg(self, message: str) -> bool:
        """向运行在指定端口的服务发送消息，如果端口被占用"""
        if self.is_port_in_use():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((self.host, self.port))
                    s.sendall(message.encode("utf-8"))
                    print(f"Message '{message}' sent successfully.")
                    return True
                except socket.error as e:
                    print(f"Failed to send message: {e}")
                    return False
        else:
            print("Port is not in use, cannot send message.")
            return False


# 示例使用
if __name__ == "__main__":
    HOST = "127.0.0.1"  # 服务器地址
    PORT = 65432  # 端口号
    TIMEOUT = 2  # 服务运行的秒数

    server = SocketServer(HOST, PORT, TIMEOUT)

    # 检查端口是否被占用，并发送消息
    if server.is_port_in_use():
        print("Port is in use, attempting to send message...")
        success = server.send_msg("Hello, this is a test message!")
        if success:
            print("Message sent successfully.")
    else:
        print("Port is not in use, starting server...")
        server.start_server()

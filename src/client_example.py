import logging

import grpc

import service_pb2
import service_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('192.168.137.129:50051') as channel:
        stub = service_pb2_grpc.TextToSpeechStub(channel)
        response = stub.speak(service_pb2.Text(text='hello world'))


if __name__ == '__main__':
    logging.basicConfig()
    run()

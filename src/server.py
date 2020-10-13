from concurrent import futures
import time
import logging

import grpc

import service_pb2
import service_pb2_grpc

from tasks import speak
import settings


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TTSService(service_pb2_grpc.TextToSpeechServicer):
    def speak(self, request, context):
        speak.delay(request.text)
        return service_pb2.TTSResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_TextToSpeechServicer_to_server(TTSService(), server)
    server.add_insecure_port(f'[::]:{settings.SERVER_PORT}')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()

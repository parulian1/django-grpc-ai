import grpc

from app.grpc_client import ai_service_pb2_grpc, ai_service_pb2


class AIClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = ai_service_pb2_grpc.AIServiceStub(self.channel)

    def analyze_text(self, text):
        request = ai_service_pb2.TextRequest(text=text)
        response = self.stub.AnalyzeText(request)
        return response.sentiment, response.keywords
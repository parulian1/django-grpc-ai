import grpc
from concurrent import futures
import ai_service_pb2
import ai_service_pb2_grpc

class AIServiceServicer(ai_service_pb2_grpc.AIServiceServicer):
    def AnalyzeText(self, request, context):
        # Perform some basic analysis (this is just a placeholder).
        sentiment = "positive" if "good" in request.text else "negative"
        keywords = request.text if type(request.text) is str else 'invalid'
        return ai_service_pb2.TextResponse(sentiment=sentiment, keywords=keywords)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ai_service_pb2_grpc.add_AIServiceServicer_to_server(AIServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

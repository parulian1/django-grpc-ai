from django.http import JsonResponse

from app.grpc_client.ai_client import AIClient


def analyze_text_view(request):
    text = request.GET.get('text', '')
    ai_client = AIClient()
    sentiment, keywords = ai_client.analyze_text(text)
    return JsonResponse({
        'sentiment': sentiment,
        'keywords': keywords.split(',')
    })
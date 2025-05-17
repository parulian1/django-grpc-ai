from django.test import TestCase, Client

class AnalyzeTextViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_analyze_text_view(self):
        query_text = 'good test'
        response = self.client.get(f'/myapp/analyze/?text={query_text}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['sentiment'], 'positive')
        self.assertIn(query_text, data['keywords'])
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from google import genai
from dotenv import load_dotenv
load_dotenv()


@csrf_exempt
def comp3(request):
    if request.method == "POST":
        body = json.loads(request.body)
        print(body)

        sentence = body.get("sentence")

        if not sentence:
            return JsonResponse({"error": "kindly provide sentence"})

        prompt = f"""You are an expert in grammar.
        Analyse the following sentence and provide a short, precise grammar correction:
        {sentence}"""

        try:
            # Client picks up GEMINI_API_KEY from environment automatically
            client = genai.Client()

            response = client.models.generate_content(
                model="gemini-flash-latest", contents=prompt
            )
            corrected_text = response.text
            return JsonResponse({
                "corrected_sentence": corrected_text,
                "status": "success"
            })

        except Exception as e:
            print(f"Gemini API error: {e}")
            return JsonResponse({"error": str(e), "status": "error"}, status=500)

    else:
        return JsonResponse({"error": "only post allowed."})


def home(request):
    return render(request, 'test1/index.html')

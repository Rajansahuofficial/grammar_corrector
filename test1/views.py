from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from google import genai
from dotenv import load_dotenv 
load_dotenv()


# def comp(request):
#     a="trying"
#     b="executed"
#     return HttpResponse("accepted"+a+b)

# def dicto(request):

#     student ={
#     "name": "Raj",

#             }
#     print(request.GET.get("kilo"))
#     print(request.GET.get("permole"))
#     return JsonResponse(student)
    

# def is_even(number):
#     return number%2==0
# @csrf_exempt
# def check_even(request):
#     # print(request.method)
#     # print(request.body)


#     if request.method=="POST":
#         data=json.loads(request.body)
#         print(data)
#         number=int(request.GET.get("number"))
#         return JsonResponse({
#             "number": number,
#             "is_even": is_even(number)
            
#         })
#     else:
#         return JsonResponse({"reason":"only post request allowed",})
    
# #2nd learning days
# @csrf_exempt
# def comp2(request):
#     if request.method=="POST":
#         body=json.loads(request.body)
#         print(body)
#         name =body.get("name")


#         data_respond={
#             "mssg": f"Hello {name}",
#             "status":"success"
#         }
#         return JsonResponse(data_respond)

#     else:
#         return JsonResponse({"error":"only post allowed",})
    
#3rd day learning 
@csrf_exempt
def comp3(request):
    if request.method=="POST":
        body=json.loads(request.body)
        print(body)

        sentence=body.get("sentence")

        if not sentence:
            return JsonResponse({"error":"kindly provide sentence"})
        




        prompt = f"""you are an expert in grammer , 
        and you have been given a sentence to analyse 
        in an appropriate manner according to grammer in short precise ,
        this is the data:
        {sentence} """
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-flash-latest", contents=prompt
        )
        corrected_text = response.text
        data_respond = {
                    "corrected_sentence": corrected_text,
                    "status": "success"
                }
        '''return JsonResponse(data_respond)
        data_respond = {
            "corrected_sentence": corrected_text,
            "status": "success"
        }'''

        return JsonResponse(data_respond)
    else:
        return JsonResponse({"error":"only post allowed."})  



def home(request):
    return HttpResponse("Grammar Corrector API Running")


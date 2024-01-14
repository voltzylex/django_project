from django.http import HttpResponse,JsonResponse
def home_page(request):
               print("Home page called")
               friends = ["Sammer","Shivam","Nitin"]
               res = {
                       "friends_list":friends
               }
               # return HttpResponse("<h1>This is home page</h1> ")
               return JsonResponse(res,safe=False)
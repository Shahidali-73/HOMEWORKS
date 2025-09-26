from django.shortcuts import render

def username_form(request):
    return render(request, "form.html")

def result_page(request):
    username = request.GET.get("username", "")
    form_data = request.GET.dict()   # convert QueryDict to normal dict
    return render(request, "result.html", {
        "username": username,
        "form_data": form_data,
    })

from django.shortcuts import render

def color_form(request):
    return render(request, "color_form.html")

def color_result(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        color = request.POST.get("color", "")
        form_data = request.POST.dict()
        return render(request, "color_result.html", {
            "name": name,
            "color": color,
            "form_data": form_data,
        })
    else:
        # If someone visits result page directly without submitting form
        return render(request, "color_form.html")

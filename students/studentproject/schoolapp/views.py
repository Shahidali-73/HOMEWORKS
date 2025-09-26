from django.shortcuts import render

def student1(request):
    student1 = [
        {"name": "Alice", "grade": "A", "passed": True},
        {"name": "Bob", "grade": "C", "passed": False},
        {"name": "Charlie", "grade": "B", "passed": True},
    ]

    return render(request, "student1.html", {"student1": student1})
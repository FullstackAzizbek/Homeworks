from django.shortcuts import render

# Create your views here.
def lessons(request):
    lesson = [
    "2.3-dars. Operators: Comparison Operators, Logical Operators",
    "2.4-dars. Control Flow",
    "2.5-dars. Functions: Python functions, Default parameters, Keyword arguments, Recursive functions, lambda function",
    "2.6-dars. Lists. Tuple",
    "2.7-dars. Lists. Tuple (davomi)",
    "2.8-dars: Dictionaries. Dictionary comprehension",
    "2.9-dars: Dictionaries. Dictionary comprehension",
    "2.10-dars: Sets",
    "3.1-dars. Modules, Packages, name_, module search path",
    "3.2-dars: Working with files",
    "3.3-dars: Exception handling, try … except",
    "3.4-dars. OOP",
    "3.5-dars. Property, delete, read only property",
    "3.6-dars: Special methods",
    "3.7-dars. Inheritance, super()",
    "3.8-dars: Multiple inheritance",
    "3.9-dars: Overriding methods. Abstract classes",
    "3.10-dars: Encapsulation. Polymorphism. Leetcode",
    "3.11-dars: Descriptors"
    ]
    return render(request, 'lessons.html', {'darslar': lesson})

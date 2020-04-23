from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'home.html'
    context = {}
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        print(post_text)
    return render(request, template_name,context)

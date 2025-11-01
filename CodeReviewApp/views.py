from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView, TemplateView
from CodeReviewApp.forms import CodeReviewForm
from CodeReviewApp.models import CodeReview
import ollama
import markdown2

# Create your views here.
class CodeReviewFormView(CreateView):
    model = CodeReview
    form_class = CodeReviewForm
    template_name = "code_review_form.html"
    success_url = "codereview-response/"

    def form_valid(self, form):
        language = form.cleaned_data['language']
        code_to_review = form.cleaned_data['code']
        self.object = form.save()
        code_review_id = CodeReview.objects.filter(language=language, code=code_to_review).first().id
        self.success_url = self.success_url+str(code_review_id)
        return HttpResponseRedirect(reverse("codereview-response", args=[code_review_id]))



class CodeReviewView(TemplateView):
    template_name = "code_review.html"
    def get(self, request, *args, **kwargs):
        code_review = CodeReview.objects.filter(id=kwargs['codereview_id']).first()
        prompt = f"You are a code review assistant. Generate a code review of the code below in the language {code_review.language}.\n Code: {code_review.code} "
        reviewed_code = ollama.generate("qwen2.5-coder:0.5b", prompt).response
        context = {
            'code': code_review.code,
            'language': code_review.language,
            'code_review': markdown2.markdown(reviewed_code),
        }
        template = loader.get_template('code_review.html')
        return HttpResponse(template.render(context, request))

class CommentView(View):
    def post(self, request, *args, **kwargs):
        comment =request.POST.get('comment')
        prev_answer = request.POST.get('prev_answer')
        prompt = f"You are a code review assistant. Respond to the below comment to the code review. \n Code review: {prev_answer} \nComment: {comment}"
        response = markdown2.markdown(ollama.generate("qwen2.5-coder:0.5b", prompt).response)
        return JsonResponse({'response': response})







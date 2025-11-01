from django.urls import path
import CodeReviewApp
from CodeReviewApp import views

urlpatterns = [
    path('codereview', views.CodeReviewFormView.as_view(), name='codereview'),
    path('codereview-response/<int:codereview_id>', views.CodeReviewView.as_view(), name='codereview-response'),
    path('comment', views.CommentView.as_view(), name='comment'),
]
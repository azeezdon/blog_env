# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .models import Course
from django.views.generic import ListView
from hitcount.views import HitCountDetailView
# Create your views here.






class CourseListView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'
    ordering = ['-publish']
    paginate_by = 4
    


class CourseDetailView(HitCountDetailView):
    model = Course
    template_name = 'course_detail.html'
    slug_url_kwarg = 'django_slug'
    slug_url_kwarg = "slug"
    slug_field = 'slug'
    count_hit = True


    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        return context





    
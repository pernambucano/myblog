from django.shortcuts import render, redirect
from .models import Post, Annotation
from django.utils import timezone
from .forms import PostForm
from .dbpedia_sparql_endpoint import DBpediaSPARQLEndpoint
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import logging
# import urllib2
import urllib.request
import urllib.parse
import urllib.error
import json


SPOTLIGHT_URL = 'http://spotlight.dbpedia.org/rest/annotate'
SPOTLIGHT_CONFIDENCE = 0.5


def post_list(request):
    posts = Post.objects.filter(
    published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Same idea as 'consult'


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()

            text = request.POST['text']
            annotator = DBpediaAnnotator()
            annotations = json.loads(annotator.annotate_text(text))
            enriched_annotations = []
            sparql_endpoint = DBpediaSPARQLEndpoint()

            post.save()
            if 'Resources' in annotations:
                for resource in annotations['Resources']:
                    resource_attribute_values = sparql_endpoint.query_attributes(
                            resource['@URI'], ['owl:Thing'] + resource['@types'].split(','))

                    for name, value in resource_attribute_values.items():
                        resource_attribute_values[name] = ", ".join(value).replace('\n', ' ')

                    anot = Annotation(URI =resource['@URI'], surfaceForm=resource['@surfaceForm'], offset=resource['@offset'], attributeValues=resource_attribute_values, post =post )
                    anot.save()
            return redirect('blog.views.post_list')

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


class DBpediaAnnotator(object):

  def annotate_text(self, text):

    parameters = {'text': text, 'confidence': SPOTLIGHT_CONFIDENCE}
    data = urllib.parse.urlencode(parameters)
    data = data.encode('utf-8')
    request = urllib.request.Request(SPOTLIGHT_URL)
    request.add_header('Accept', 'application/json')
    #request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
    response = urllib.request.urlopen(request, data)
    #annotations = json.load(response)
    annotation = ""
    with urllib.request.urlopen(request, data) as f:
        annotation = f.read().decode('utf-8')


    return annotation


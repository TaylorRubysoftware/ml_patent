from django.shortcuts import render
from django.http import HttpResponse
import json
import cPickle as pickle
from logic.search import *
from logic.generate_hash import *


def index(request):
    return render(request, 'search/index.html')


def search(request):
    dictionary = load_dictionary('data/dictionary.txt')
    try:
        request_words = request.GET.keys()[0].split()
        bow = create_bag_of_words(dictionary, request_words)
        hash = calculate_hash('data/autoencoder', bow)
        with open('data/db2', "rb") as file:
            database = pickle.load(file)
        results = find_closest_patents(database, hash, patents=8)
        for r in results:
            del r['hash']
            r['url'] = generate_url('http://www.freepatentsonline.com/', r['id'])
        return HttpResponse(json.dumps({'results': results}), content_type="application/json")
    except Exception as inst:
        print inst

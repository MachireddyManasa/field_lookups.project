from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.functions import Length


def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.exclude(topic_name='Hockey')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)
def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2023-06-10')
    LOA=AccessRecord.objects.filter(date__gte='2023-06-10')
    LOA=AccessRecord.objects.filter(date__lt='2023-06-10')
    LOA=AccessRecord.objects.filter(date__lte='2023-06-10')
    d={'access':LOA}
    return render(request,'display_access.html',d)
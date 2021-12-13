from django.shortcuts import get_object_or_404, render
from . models import Category, Course, Tag



def courses(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    current_user = request.user

    if category_slug != None:
        # first param is our Category model, second one is the slug field of Category model
        # look Category model for this.
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(available=True, category = category_page)
    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(available=True, tags=tag_page)
    else:
        if current_user.is_authenticated:
            enrolled_courses = current_user.joined_courses.all()
            courses = Course.objects.all().order_by('-date')
            for course in enrolled_courses:
                courses = courses.exclude(id=course.id)
        else:
            courses = Course.objects.all().order_by('-date')

    
    context = {
        'courses': courses,
        'categories': category_list,
        'tags': tag_list,
    }

    return render(request, 'courses.html', context)    


def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug = category_slug, id = course_id)
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if current_user.is_authenticated:
        enrolled_courses = current_user.joined_courses.all()
    else:
        enrolled_courses = courses


    context = {
        'course': course,
        'enrolled_courses':enrolled_courses,
        'categories':categories,
        'tags': tags,
    }
    
    return render(request, 'course.html', context)


def search(request):
    # take the description field from Course model and check it has a input text
    # which is matching with that description
    # we can take input values from request object but make sure that
    # you create url and put this inside the action attribute of form
    # then we need to reach input value 
    # we can reach by its name field('search')
    # after all we capture value by request.GET['search]
    courses = Course.objects.filter(description__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'courses.html', context)


# Create your views here.
# def courses(request):
#     courses = Course.objects.all().order_by('-date')
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses': courses,
#         'categories': categories,
#         'tags': tags,
#     }
#     return render(request, 'courses.html', context)


# def category_list(request, category_slug):
#     # course'dan category ulaşmak için 2 alt çizgi kullandık
#     courses = Course.objects.all().filter(category__slug = category_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses': courses,
#         'categories': categories,
#         'tags': tags,
#     }
#     return render(request, 'courses.html', context)


# def tag_list(request, tag_slug):
#     # course'dan tag'in slug fieldına  ulaşmak için 2 alt çizgi kullandık
#     # look for Course model and its filed of tags so we wrote tags__slug
#     courses = Course.objects.all().filter(tags__slug = tag_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     context = {
#         'courses': courses,
#         'categories': categories,
#         'tags': tags,
#     }
#     return render(request, 'courses.html', context)



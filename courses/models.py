from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher


# Many-to-One relations
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name


# Many-to-Many relations
class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)


    def __str__(self):
        return self.name


class Course(models.Model):
    # verbose_name is the name that will be shown on the Admin page
    # help_text is the text that will be shown on the Admin page
    # why help_text is used is that it consists of more exlplanation about that column
    # connect Teacher model
    # if we delete teacher then delete her/his courses as well with CASCADE
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, verbose_name='Course Name')
    # connect Category model
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    # many-to-may
    tags = models.ManyToManyField(Tag, blank=True,)
    students = models.ManyToManyField(User, blank=True, related_name='joined_courses')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

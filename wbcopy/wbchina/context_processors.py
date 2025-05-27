from .models import Category

def categories(request):
    """
    Context processor to make all categories available in templates
    """
    categories_list = Category.objects.all()
    for category in categories_list:
        if not category.slug:
            category.save()
    
    return {
        'categories': Category.objects.exclude(slug='').filter(parent=None)
    } 
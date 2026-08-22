from blog.services import get_public_categories, get_public_pages


def blog_context(request):
    return {
        "categories": get_public_categories(),
        "pages": get_public_pages(),
    }

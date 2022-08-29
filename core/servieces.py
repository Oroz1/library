from core.models import Book


class IncreaseViewsBookMixin(object):
    
      def dispatch(self, request, id, *args, **kwargs):
        book = Book.objects.get(id=id)
        book.views += 1
        book.save()
        return super().dispatch(request, *args, **kwargs)
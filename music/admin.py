from django.contrib import admin
from .models import Album, Song
from .models import Post
from .models import Stock
admin.site.register(Stock)

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Post)




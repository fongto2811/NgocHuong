from django.db import models
from django import forms
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.models import register_snippet


class NewIndexPage(Page):
    page_description = "Tạo trang danh sách tin tức"
    content_panels = Page.content_panels
    def get_context(self, request):
        # Cập nhật ngữ cảnh để chỉ bao gồm các bài đăng đã xuất bản, được sắp xếp theo niên đại ngược
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
    class Meta:
        verbose_name = "Menu tin tức"

class NewPage(Page):
    page_description = "Tạo trang chi tiết tin tức"
    date = models.DateField("Post date")
    intro = models.CharField(max_length=300)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    body = RichTextField(blank=True)
    authors = ParentalManyToManyField('blog.Author', blank=True)
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
        
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = "Chi tiết tin tức"
   
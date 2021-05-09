from django.contrib import admin

# Register your models here.
from corpus.models import File, Sentence, Tagging
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class TaggingInline(admin.TabularInline):
    model = Tagging
    extra = 1

class TaggingAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'word', 'pos')
    list_filter = ['pos']
    search_fields = ['word']

class SentenceInline(admin.TabularInline):
    model = Sentence
    extra = 1

class SentenceAdmin(ImportExportMixin, admin.ModelAdmin):
    inlines = [TaggingInline]
    list_display = ('id', 'file', 'sentence_text')
    list_display_links = ('id','sentence_text')
    list_filter = ['file']
    search_fields = ['sentence_text']

class FileAdmin(admin.ModelAdmin):
    #fields = ['id', 'file_name']
    inlines = [SentenceInline]
    list_display = ('id', 'file_name')
    list_display_links = ('id', 'file_name')

admin.site.register(File, FileAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Tagging, TaggingAdmin)




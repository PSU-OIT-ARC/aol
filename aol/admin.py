from django.utils.translation import gettext_lazy as _
from django.contrib.flatpages import models as flatpages_models
from django.contrib.flatpages import forms as flatpages_forms
from django.contrib.flatpages import admin as flatpages_admin
from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from aol.lakes import models as lakes_models
from aol.lakes import admin as lakes_admin
from aol.documents import models as documents_models
from aol.documents import admin as documents_admin
from aol.photos import models as photos_models
from aol.photos import admin as photos_admin
from aol.plants import models as plants_models
from aol.plants import admin as plants_admin
from aol.mussels import models as mussels_models
from aol.mussels import admin as mussels_admin


class AdminSite(admin.AdminSite):
    site_header = "Atlas of Oregon Lakes Administration"

admin_site = AdminSite(name='admin')

# lake admin registration
admin_site.register(lakes_models.County)
admin_site.register(lakes_models.FishingZone)
admin_site.register(lakes_models.Lake, lakes_admin.LakeAdmin)
# document admin registration
admin_site.register(documents_models.Document, documents_admin.DocumentAdmin)
# photo admin registration
admin_site.register(photos_models.Photo, photos_admin.PhotoAdmin)
# plant admin registration
admin_site.register(plants_models.Plant)
admin_site.register(plants_models.PlantObservation, plants_admin.PlantObservationAdmin)
# mussel admin registration
admin_site.register(mussels_models.ReportingAgency)
admin_site.register(mussels_models.Mussel)
admin_site.register(mussels_models.MusselObservation, mussels_admin.MusselObservationAdmin)
# flatpages admin registration
class FlatPageForm(flatpages_forms.FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())

class FlatPageAdmin(flatpages_admin.FlatPageAdmin):
    list_display = ('url', 'title')
    list_filter = ()
    search_fields = ('url', 'title')

    form = FlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
    )

admin_site.register(flatpages_models.FlatPage, FlatPageAdmin)

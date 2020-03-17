from django import forms
from django.forms import widgets

from .models import Journal


class JournalStatusWidget(widgets.Select):

    ICONS = {
        Journal.Status.DIDNT_READ: {'icon': 'fa-plus-circle', 'color': '#0e70a0'},
        Journal.Status.READING: {'icon': 'fa-play-circle', 'color': '#2ebf00'},
        Journal.Status.READ: {'icon': 'fa-check-circle', 'color': 'green'},
        Journal.Status.STOPPED: {'icon': 'fa-stop-circle', 'color': '#c71414'}
    }

    def icon(self, value):
        icon = JournalStatusWidget.ICONS[value]
        title = self.choices[value-1][1]
        return f'<i class="fas {icon["icon"]} fa-lg" style="color: {icon["color"]}" title="{title}"></i>'


class JournalAdminForm(forms.ModelForm):

    class Meta:
        model = Journal
        widgets = {
            'status': JournalStatusWidget()
        }
        fields = '__all__'

from django import forms

from app.widgets import JournalStatusWidget
from .models import Journal


class BookJournalStatusWidget(JournalStatusWidget):
    ICONS = {
        Journal.Status.DIDNT_READ: {'icon': '', 'color': '#0e70a0'},
        Journal.Status.READING: {'icon': 'fa-play-circle', 'color': '#2ebf00'},
        Journal.Status.READ: {'icon': 'fa-check-circle', 'color': 'green'},
        Journal.Status.STOPPED: {'icon': 'fa-stop-circle', 'color': '#c71414'}
    }


class JournalAdminForm(forms.ModelForm):
    class Meta:
        model = Journal
        widgets = {
            'status': BookJournalStatusWidget()
        }
        fields = '__all__'

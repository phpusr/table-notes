from django import forms

from app.widgets import JournalStatusWidget
from .models import Journal


class TvSeriesJournalStatusWidget(JournalStatusWidget):
    ICONS = {
        Journal.Status.WATCHING: {'icon': 'fa-play-circle', 'color': '#2ebf00'},
        Journal.Status.WAITING: {'icon': 'fa-pause-circle', 'color': '#0e70a0'},
        Journal.Status.DONE: {'icon': 'fa-check-circle', 'color': 'green'},
        Journal.Status.STOPPED: {'icon': 'fa-stop-circle', 'color': 'gray'},
        Journal.Status.DIDNT_WATCH: {'icon': '', 'color': '#0e70a0'}
    }


class JournalAdminForm(forms.ModelForm):
    class Meta:
        model = Journal
        widgets = {
            'status': TvSeriesJournalStatusWidget()
        }
        fields = '__all__'

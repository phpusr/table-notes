from django import forms

from .models import Journal


class JournalStatusWidget(forms.widgets.Select):
    ICONS = {
        Journal.Status.WATCHING: {'icon': 'fa-play-circle', 'color': '#2ebf00'},
        Journal.Status.WAITING: {'icon': 'fa-pause-circle', 'color': '#0e70a0'},
        Journal.Status.DONE: {'icon': 'fa-check-circle', 'color': 'green'},
        Journal.Status.STOPPED: {'icon': 'fa-stop-circle', 'color': 'gray'},
        Journal.Status.DIDNT_WATCH: {'icon': '', 'color': '#0e70a0'}
    }

    def icon(self, value):
        icon = JournalStatusWidget.ICONS[value]
        title = self.choices[value-1][1]
        return f'<i class="fas {icon["icon"]} fa" style="color: {icon["color"]}" title="{title}"></i>'


class JournalAdminForm(forms.ModelForm):
    class Meta:
        model = Journal
        widgets = {
            'status': JournalStatusWidget()
        }
        fields = '__all__'

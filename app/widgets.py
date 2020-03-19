from django import forms


class JournalStatusWidget(forms.widgets.Select):
    ICONS = {}

    def icon(self, value):
        icon = self.ICONS[value]
        title = self.choices[value-1][1]
        return f'<i class="fas {icon["icon"]} fa" style="color: {icon["color"]}" title="{title}"></i>'

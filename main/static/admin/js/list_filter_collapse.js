/*
* src: http://qaru.site/questions/3688420/trying-to-showhide-the-changelist-filter-in-django-admin
*/

(function($) {
    $(document).ready($ => {
        $("tr input.action-select").actions()
        $('<div id="show-filters" style="float: right;"><a href="#">Show filters</a></p>').prependTo('div.actions')
        $('#changelist-filter h2').html('<a style="color: white;" id="hide-filters" href="#">Filter &rarr;</a>')

        $('#show-filters').click(() => {
            $('#changelist-filter').show('fast')
            $('#changelist').addClass('filtered')
            $('#show-filters').hide()
        })

        $('#hide-filters').click(() => {
            $('#changelist-filter').hide('fast')
            $('#show-filters').show()
            $('#changelist').removeClass('filtered')
        })

        $('#hide-filters').click();
    })
})($)

/**
 * Add button for show and hide filters in actions menu
 * src: http://qaru.site/questions/3688420/trying-to-showhide-the-changelist-filter-in-django-admin
*/

window.onload = () => {
    (function($) {
        $(`
          <div id="show-filters" style="float: right">
            <a href="#">Show filters</a>
          </div>
        `).prependTo('div.actions')
        $('#changelist-filter h2').html('<a style="color: white;" id="hide-filters" href="#">Filters &rarr;</a>')

        $('#show-filters').click(() => {
            $('#changelist-filter').show('fast')
            $('#changelist').addClass('filtered')
            $('#show-filters').hide()
        })

        $('#hide-filters')
          .click(() => {
                $('#changelist-filter').hide('fast')
                $('#show-filters').show()
                $('#changelist').removeClass('filtered')
            })
          .click()
    })(django.jQuery)
}

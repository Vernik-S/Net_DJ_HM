from django import template

register = template.Library()


@register.filter
def next_date(page):
    if page.has_next():
        return page.paginator.get_page(page.next_page_number()).object_list[0]
    else:
        return None


@register.filter
def prev_date(page):
    if page.has_previous():
        return page.paginator.get_page(page.previous_page_number()).object_list[0]
    else:
        return None

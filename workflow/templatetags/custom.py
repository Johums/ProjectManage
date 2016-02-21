# -*- coding: utf-8 -*-
from django import template
from django.utils import safestring

register = template.Library()


@register.filter
def multi_menu(menu, move=0):
    html_content = """
        <ul class="nav nav-pills nav-stacked" style="margin-left: %spx" >
    """ % move

    for k, v in menu.items():
        html_content += """
        <li data-toggle="collapse" data-target=".demo">
            <a href="{1}"><small>{2}</small></a>
        </li>
        """.format(*k)
        if v:
            html_content += multi_menu(v, move + 20)

    html_content += """
        </ul>
    """
    return safestring.mark_safe(html_content)

import tw2.core as twc
from tw2.core.resources import encoder

import tw2.jqplugins.ui
import tw2.jqplugins.ui.base

import base

class MenuWidget(tw2.jqplugins.ui.base.JQueryUIWidget, twc.DisplayOnlyWidget):
    """ Slidey menu that I made just for you!

    This is *quite* alpha still.  Please play with it and enhance it if you
    like.

    options::

        - width:  -- the width of the menu.

    """

    resources = [
        tw2.jquery.jquery_js,
        tw2.jqplugins.ui.jquery_ui_js,
        tw2.jqplugins.ui.jquery_ui_css,
        base.slidey_js,
        base.slidey_css,
    ]

    template = "mako:tw2.slideymenu.templates.menu"

    items = twc.Param('A recursive dictionary of menu entries', default=[])
    label = twc.Param('Label for the menu-show button', default='Menu')
    options = twc.Param('Options.', default={})

    def prepare(self):
        super(MenuWidget, self).prepare()
        self._options = encoder.encode(self.options)

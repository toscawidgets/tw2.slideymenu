"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from widgets import MenuWidget

class DemoMenuWidget(MenuWidget):
    items = [
        {
            'label' : 'An item',
            'href'  : "javascript:alert('clicked -- yes');",
        },{
            'label' : 'Another item',
            'href'  : "javascript:alert('clicked -- yes');",
        },{
            'label' : 'An item with no href',
        }
    ]

    label = 'A slidey menu'
    options = {
        'width' : '500px'
    }


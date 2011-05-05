
# TW2 proper imports
import tw2.core as twc

slidey_js = twc.JSLink(modname=__name__, filename='static/js/slidey.js')
slidey_css = twc.CSSLink(modname=__name__, filename='static/css/slidey.css')

__all__ = ['slidey_js']

from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('bootstrap', 'resources')

bootstrap_css = Resource(library, 'css/bootstrap.css',
                         minified='css/bootstrap.min.css')

bootstrap_theme = Resource(library, 'css/bootstrap-theme.css',
                           minified='css/bootstrap-theme.min.css',
                           depends=[bootstrap_css])

bootstrap_js = Resource(library, 'js/bootstrap.js',
                        minified='js/bootstrap.min.js',
                        bottom=True,
                        depends=[jquery, ])

bootstrap = Group([bootstrap_css, bootstrap_js])

from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('bootstrap', 'resources')

bootstrap_css = Resource(library, 'bootstrap.css',
                         minified='bootstrap.min.css')
bootstrap_responsive_css = Resource(library, 'bootstrap.responsive.css',
                                    minified='bootstrap.min.responsive.css',
                                    depends=[bootstrap_css,],)
bootstrap_js = Resource(library, 'bootstrap.js',
                        minified='bootstrap.min.js',
                        depends=[jquery,])

bootstrap = Group([bootstrap_css, bootstrap_js])

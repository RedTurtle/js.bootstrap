from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('bootstrap', 'resources')

bootstrap_css = Resource(library, 'bootstrap.css',
                         minified='bootstrap.min.css')
bootstrap_alerts = Resource(library, 'bootstrap-alerts.js',
                            depends=[jquery,])
bootstrap_dropdown = Resource(library, 'bootstrap-dropdown.js',
                              depends=[jquery,])
bootstrap_modal = Resource(library, 'bootstrap-modal.js',
                           depends=[jquery,])
bootstrap_twipsy = Resource(library, 'bootstrap-twipsy.js',
                            depends=[jquery,])
bootstrap_popover = Resource(library, 'bootstrap-popover.js',
                             depends=[jquery, bootstrap_twipsy])
bootstrap_scrollspy = Resource(library, 'bootstrap-scrollspy.js',
                               depends=[jquery,])
bootstrap_tabs = Resource(library, 'bootstrap-tabs.js',
                          depends=[jquery,])
bootstrap_buttons = Resource(library, 'bootstrap-buttons.js',
                          depends=[jquery,])

bootstrap = Group([bootstrap_css, bootstrap_alerts, bootstrap_dropdown,
                   bootstrap_modal, bootstrap_popover, bootstrap_scrollspy,
                   bootstrap_tabs, bootstrap_twipsy, bootstrap_buttons])

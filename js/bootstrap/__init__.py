from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('bootstrap', 'resources')

bootstrap_css = Resource(library, 'bootstrap.css',
                         minified='bootstrap.min.css')

bootstrap_alerts = Resource(library, 'bootstrap-alert.js',
                            depends=[jquery,])
bootstrap_buttons = Resource(library, 'bootstrap-button.js',
                          depends=[jquery,])
bootstrap_dropdown = Resource(library, 'bootstrap-dropdown.js',
                              depends=[jquery,])
bootstrap_modal = Resource(library, 'bootstrap-modal.js',
                           depends=[jquery,])
bootstrap_tabs = Resource(library, 'bootstrap-tab.js',
                          depends=[jquery,])
bootstrap_tooltip = Resource(library, 'bootstrap-tooltip.js',
                             depends=[jquery,])
bootstrap_popover = Resource(library, 'bootstrap-popover.js',
                             depends=[jquery, bootstrap_tooltip])
bootstrap_scrollspy = Resource(library, 'bootstrap-scrollspy.js',
                               depends=[jquery,])
bootstrap_carousel = Resource(library, 'bootstrap-carousel.js',
                               depends=[jquery,])
bootstrap_collapse = Resource(library, 'bootstrap-collapse.js',
                               depends=[jquery,])
bootstrap_transition = Resource(library, 'bootstrap-transition.js',
                               depends=[jquery,])
bootstrap_typeahead = Resource(library, 'bootstrap-typeahead.js',
                               depends=[jquery,])

bootstrap_responsive = Resource(library, 'bootstrap-responsive.css', depends=[bootstrap_css,])

bootstrap = Group([bootstrap_css, bootstrap_alerts, bootstrap_dropdown,
                   bootstrap_modal, bootstrap_popover, bootstrap_scrollspy,
                   bootstrap_tabs, bootstrap_tooltip, bootstrap_buttons,
                   bootstrap_carousel, bootstrap_collapse, bootstrap_transition, bootstrap_typeahead, bootstrap_responsive
                   ])

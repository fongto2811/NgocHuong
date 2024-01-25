from django.utils.safestring import mark_safe
from .draftail_extensions import register_inline_styling, register_block_feature
from wagtail import hooks

@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        r'wagtailadmin\icons\decrease-font.svg',
        r'wagtailadmin\icons\increase-font.svg',
        r'wagtailadmin\icons\right-align.svg',
        r'wagtailadmin\icons\left-align.svg',
        r'wagtailadmin\icons\centre-align.svg',
    ]

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return mark_safe(
    """
    <style>
        .Draftail-Toolbar {
            /* float toolbar so always visible */
            position: sticky !important;
            top: calc(0.2rem + 50px) !important;
            z-index: 2 !important;
        }
        @media screen and (max-width: 800px) {
            .Draftail-Toolbar {
                /* double top height when top menu wraps at 800px */
                top: calc(0.2rem + 100px) !important;
            }
        }
        .Draftail-ToolbarGroup, .tab-content--comments-enabled .Draftail-CommentControl {
            /* allow toolbar button groups to wrap */
            display: contents !important;
        }
    </style>
    """
    )

@hooks.register('insert_editor_js')
def editor_js():
    return mark_safe(
    """
    <script>
        window.localStorage.setItem("wagtail:draftail-toolbar", "sticky");
    </script>
    """
)

@hooks.register("register_rich_text_features")
def register_underline_styling(features):
    register_inline_styling(
        features=features,
        feature_name='underline',
        type_='UNDERLINE',
        tag='u',
        description='Underline',
        label='U̲'
    )

@hooks.register("register_rich_text_features")
def register_larger_styling(features):
    register_inline_styling(
        features=features,
        feature_name='larger',
        type_='LARGER',
        tag='span',
        format='style="font-size:larger;"',
        editor_style={'font-size':'larger'},
        description='Increase Font',
        icon='increase-font'
    )

@hooks.register("register_rich_text_features")
def register_smaller_styling(features):
    register_inline_styling(
        features=features,
        feature_name='smaller',
        type_='SMALLER',
        tag='span',
        format='style="font-size:smaller;"',
        editor_style={'font-size':'smaller'},
        description='Decrease Font',
        icon='decrease-font'
    )

@hooks.register('register_rich_text_features')
def register_align_left_feature(features):
    register_block_feature(
        features=features,
        feature_name='left-align',
        type_='LEFT-ALIGN',
        description='Left align text',
        css_class='text-start',
        element='p',
        icon='left-align'
    )
    
@hooks.register('register_rich_text_features')
def register_align_centre_feature(features):
    register_block_feature(
        features=features,
        feature_name='centre-align',
        type_='CENTRE-ALIGN',
        description='Centre align text',
        css_class='text-center',
        element='p',
        icon='centre-align'
    )
    
@hooks.register('register_rich_text_features')
def register_align_right_feature(features):
    register_block_feature(
        features=features,
        feature_name='right-align',
        type_='RIGHT-ALIGN',
        description='Right align text',
        css_class='text-end',
        element='p',
        icon='right-align'
    )
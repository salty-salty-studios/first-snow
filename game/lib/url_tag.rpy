init python:
    def url_tag(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, u'a={}'.format(contents[0][1])),
        ] + contents + [
            (renpy.TEXT_TAG, u'/a')
        ]
    config.custom_text_tags['url'] = url_tag

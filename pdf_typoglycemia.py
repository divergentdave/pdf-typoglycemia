import random
import re

import pdf_redactor

WORD_RE = re.compile("[A-Za-z]{4,}")


def typo_word(match):
    word = list(match.group(0))
    middle = word[1:-1]
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]


def typo_text(text):
    return WORD_RE.sub(typo_word, text)


def typo_xml(doc):
    if doc is None:
        return None
    for e in doc.iter():
        for key, value in list(e.items()):
            e.attrib[key] = typo_text(value)
        if e.text is not None:
            e.text = typo_text(e.text)
        if e.tail is not None:
            e.tail = typo_text(e.tail)
    return doc

options = pdf_redactor.RedactorOptions()

options.metadata_filters = {
    "DEFAULT": [lambda value: typo_text(value)]
}

options.xmp_filters = [typo_xml]

options.content_filters = [
    (
        WORD_RE,
        lambda match: typo_text(match.group(0))
    ),
]

pdf_redactor.redactor(options)

r"""°°°
# An Interactive Autocomplete Interface
## Chris Tralie
°°°"""
# |%%--%%| <v0894lV1nw|ju1c7J4oeR>

%load_ext autoreload
%autoreload 2

import numpy as np
import ipywidgets as widgets
from IPython.display import display
from trie import *


autocomplete = Autocomplete("words.txt")
max_terms = 20

    
alist = widgets.Select(
    options=[],
    rows=max_terms,
    description='Autocompletions:',
    disabled=False
)

def reset_options(c):
    alist.options = tuple([chr(ord("a")+i) for i in range(20)])


wtext = widgets.Textarea(
    value='',
    placeholder='Type something',
    description='String:',
    disabled=False
)

def typing(c):
    s = wtext.value
    if len(s) > 1:
        terms = autocomplete.all_matches(s)
        alist.options = tuple(terms[0:max_terms])
    else:
        alist.options = tuple([])

wtext.observe(typing)



display(wtext)
display(alist)

# |%%--%%| <ju1c7J4oeR|0zTrAw1ZH0>



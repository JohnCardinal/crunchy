"""  Crunchy load remote tutorial plugin.

Creates a form allowing to specify the URL of a tutorial to be loaded
by Crunchy.

This module is meant to be used as an example of how to create a custom
Crunchy plugin; it probably contains more comments than necessary
for people familiar with the Crunchy plugin architecture.
"""

# All plugins should import the crunchy plugin API
import src.CrunchyPlugin as CrunchyPlugin

# The set of other "widgets/services" required from other plugins
requires = set(["/remote"])

def register():
    """The register() function is required for all plugins.
       In this case, we need to register a single type of 'action':
          a custom 'vlam handler' designed to tell Crunchy how to
          interpret the special Crunchy markup.
       """
    # 'load_remote' only appears inside <span> elements, using the notation
    # <span title='load_remote'>
    CrunchyPlugin.register_vlam_handler("span", "load_remote", insert_load_remote)

def insert_load_remote(page, parent, uid, vlam):
    form = CrunchyPlugin.SubElement(parent, 'form', name='url', size='80', method='get',
                       action='/remote')
    input1 = CrunchyPlugin.SubElement(form, 'input', name='url', size='80',
                           value=parent.text)
    input2 = CrunchyPlugin.SubElement(form, 'input', type='submit',
                           value='Load remote tutorial')
    input2.attrib['class'] = 'crunchy'
    parent.text = ' '

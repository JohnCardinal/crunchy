"""  Crunchy interpreter plugin.

From some Python code simulating a Python interpreter session
contained inside a <pre> element, it inserts an actual interpreter
for user interaction.

This module is meant to be used as an example of how to create a custom
Crunchy plugin; it probably contains more comments than necessary
for people familiar with the Crunchy plugin architecture.
"""

import sys

# All plugins should import the crunchy plugin API
import CrunchyPlugin

# The set of other "widgets/services" required from other plugins
requires = set(["io_widget", "/exec"])

def register():
    """The register() function is required for all plugins.
       In this case, we need to register only two type of 'actions':
        a custom 'vlam handler' designed to tell Crunchy how to
          interpret the special Crunchy markup.
       """
    # 'interpreter' only appears inside <pre> elements, using the notation
    # <pre title='interpreter ...'>
    CrunchyPlugin.register_vlam_handler("pre", "interpreter", insert_interpreter)

def insert_interpreter(page, elem, uid, vlam):
    """inserts an interpreter (actually the js code to initialise an interpreter)"""
    # first we need to make sure that the required javacript code is in the page:
    if not page.includes("interp_included"):
        page.add_include("interp_included")
        page.add_js_code(interp_js)
    # then we can go ahead and add html markup, extracting the Python
    # code to be executed in the process - we will not need this code;
    # this could change in a future version where we could add a button to
    # have the code automatically "injected" and executed by the
    # interpreter, thus saving some typing by the user.
    code, markup = CrunchyPlugin.services.style_pycode(page, elem)
    # reset the original element to use it as a container.  For those
    # familiar with dealing with ElementTree Elements, in other context,
    # note that the style_doctest() method extracted all of the existing
    # text, removing any original markup (and other elements), so that we
    # do not need to save either the "text" attribute or the "tail" one
    # before resetting the element.
    elem.clear()
    elem.tag = "div"
    if not "no-pre" in vlam:
        elem.insert(0, markup)
    # the javascript code required to initialise this Python interpreter
    page.add_js_code('init_interp("%s");' % uid)
    # finally, an output subwidget:
    CrunchyPlugin.services.insert_io_subwidget(page, elem, uid)

interp_js = r"""
function init_interp(uid){
    code = "import interpreter\ninterpreter.BorgConsole().interact('Crunchy interpreter (Python version %s)')";
    var j = new XMLHttpRequest();
    j.open("POST", "/exec?uid="+uid, false);
    j.send(code);
};
"""%(sys.version.split(" ")[0])
from zope.interface import implementer
from makeup.platform.interfaces import IArtist
from plone.dexterity.content import Container


@implementer(IArtist)
class Artist(Container):
    """MakeupArtist Content Type"""

def on_add(obj, evt):
    # This triggers also on the container creation, not only on save props!
    # review_state = obj.portal_workflow.getInfoFor(obj, "review_state")
    # import pdb;pdb.set_trace()
    # if not review_state == "published":
    #     obj.portal_workflow.doActionFor(obj,"publish")

    pass

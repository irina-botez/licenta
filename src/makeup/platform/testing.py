# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import makeup.platform


class MakeupPlatformLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=makeup.platform)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'makeup.platform:default')


MAKEUP_PLATFORM_FIXTURE = MakeupPlatformLayer()


MAKEUP_PLATFORM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MAKEUP_PLATFORM_FIXTURE,),
    name='MakeupPlatformLayer:IntegrationTesting'
)


MAKEUP_PLATFORM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MAKEUP_PLATFORM_FIXTURE,),
    name='MakeupPlatformLayer:FunctionalTesting'
)


MAKEUP_PLATFORM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MAKEUP_PLATFORM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MakeupPlatformLayer:AcceptanceTesting'
)

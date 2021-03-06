# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from makeup.platform.interfaces import Imakeup
from makeup.platform.testing import MAKEUP_PLATFORM_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class makeupIntegrationTest(unittest.TestCase):

    layer = MAKEUP_PLATFORM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='makeup')
        schema = fti.lookupSchema()
        self.assertEqual(Imakeup, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='makeup')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='makeup')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(Imakeup.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='makeup',
            id='makeup',
        )
        self.assertTrue(Imakeup.providedBy(obj))

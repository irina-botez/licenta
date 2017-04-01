# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from makeup.platform.testing import MAKEUP_PLATFORM_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that makeup.platform is properly installed."""

    layer = MAKEUP_PLATFORM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if makeup.platform is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'makeup.platform'))

    def test_browserlayer(self):
        """Test that IMakeupPlatformLayer is registered."""
        from makeup.platform.interfaces import (
            IMakeupPlatformLayer)
        from plone.browserlayer import utils
        self.assertIn(IMakeupPlatformLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MAKEUP_PLATFORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['makeup.platform'])

    def test_product_uninstalled(self):
        """Test if makeup.platform is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'makeup.platform'))

    def test_browserlayer_removed(self):
        """Test that IMakeupPlatformLayer is removed."""
        from makeup.platform.interfaces import \
            IMakeupPlatformLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMakeupPlatformLayer, utils.registered_layers())

import test_helper
import unittest
from unittest import TestCase

from event_manager import EventManager

class EventManagerTest(TestCase):

    def testRegisterListener(self):
        em = EventManager()
        em.registerListener("foo")
        self.assertTrue("foo" in em.listeners)

    def testUnregisterListener(self):
        em = EventManager()
        em.registerListener("foo")
        self.assertTrue("foo" in em.listeners)

        em.unregisterListener("foo")
        self.assertFalse("foo" in em.listeners)

    def testPost(self):
        self.fail("not implemented")

if __name__ == "__main__":
    unittest.main()

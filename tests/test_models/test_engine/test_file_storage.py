#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import os
import unittest
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_and_all(self):
        """Test new() adds object and all() returns it"""
        obj = BaseModel()
        storage.new(obj)
        all_objs = storage.all()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], obj)

    def test_save_and_reload(self):
        """Test save writes to file and reload restores objects"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

        # Clear objects and reload
        storage.all().clear()
        storage.reload()
        all_objs = storage.all()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].id, obj.id)

    def tearDown(self):
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")


if __name__ == "__main__":
    unittest.main()

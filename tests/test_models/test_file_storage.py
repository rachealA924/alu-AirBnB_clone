#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        # Clear objects and remove file if exists
        self.storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_and_all(self):
        """Test new() adds object and all() returns it"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], obj)

    def test_save_and_reload(self):
        """Test save writes to file and reload restores objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        # Clear objects and reload
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        all_objs = self.storage.all()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].id, obj.id)
        self.assertEqual(all_objs[key].created_at, obj.created_at)
        self.assertEqual(all_objs[key].updated_at, obj.updated_at)

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists("file.json"):
            os.remove("file.json")


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_reload_no_file(self):
        pass


if __name__ == "__main__":
    unittest.main()



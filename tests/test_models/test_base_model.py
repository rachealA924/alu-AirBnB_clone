#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_instance_creation(self):
        """Test BaseModel instance creation and attribute types."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        model_key = f"BaseModel.{model.id}"  # Use correct key format
        self.assertIsInstance(
            model.created_at,
            type(storage.all()[model_key].created_at)
        )
        self.assertIsInstance(
            model.updated_at,
            type(storage.all()[model_key].updated_at)
        )

    def test_to_dict(self):
        """Test dictionary representation of BaseModel."""
        model = BaseModel()
        model.name = "Test"
        model.number = 42
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["name"], "Test")
        self.assertEqual(model_dict["number"], 42)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_str_method(self):
        """Test __str__ method."""
        model = BaseModel()
        output = str(model)
        self.assertIn("[BaseModel]", output)
        self.assertIn(model.id, output)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at."""
        model = BaseModel()
        old_time = model.updated_at
        import time
        time.sleep(0.01)  # Add a short delay
        model.save()
        self.assertNotEqual(old_time, model.updated_at)

    def test_instance_from_dict(self):
        """Test creating instance from dictionary."""
        model = BaseModel()
        model.name = "Example"
        model.number = 10
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.number, model.number)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)


if __name__ == "__main__":
    unittest.main()

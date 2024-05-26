#!/usr/bin/python3
"""Initializes this folder"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
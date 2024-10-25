"""
Unit tests for the PluginLoader class.
"""

import pytest
from app.plugin_loader import PluginLoader

@pytest.fixture
def plugin_loader():
    """Fixture to create a PluginLoader instance."""
    return PluginLoader(plugin_dir='app/plugins')

def test_load_existing_plugin(plugin_loader):
    """Test loading an existing plugin."""
    # Assume 'example_plugin' exists in the plugins directory
    plugin_loader.load_plugin('square')
    assert 'square' in plugin_loader.plugins

def test_load_non_existing_plugin(plugin_loader):
    """Test loading a non-existing plugin."""
    with pytest.raises(ImportError):
        plugin_loader.load_plugin('non_existing_plugin')

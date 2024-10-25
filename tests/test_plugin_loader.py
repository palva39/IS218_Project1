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
    plugin_loader.load_plugin('example_plugin')
    assert 'example_plugin' in plugin_loader.plugins

def test_load_non_existing_plugin(plugin_loader):
    """Test loading a non-existing plugin."""
    with pytest.raises(ImportError):
        plugin_loader.load_plugin('non_existing_plugin')

def test_reload_existing_plugin(plugin_loader):
    """Test re-loading an already loaded plugin."""
    # Load the plugin once
    plugin_loader.load_plugin('example_plugin')
    assert 'example_plugin' in plugin_loader.plugins

    # Load it again to ensure it doesn't cause an error
    plugin_loader.load_plugin('example_plugin')
    assert 'example_plugin' in plugin_loader.plugins

def test_load_invalid_plugin(plugin_loader):
    """Test loading an invalid plugin with unexpected errors."""
    with pytest.raises(ImportError):
        plugin_loader.load_plugin('invalid_plugin_with_error')

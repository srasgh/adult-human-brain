#!/usr/bin/env python3
"""
Test script to verify cytograph installation and basic functionality
"""

import sys
import cytograph

def test_cytograph():
    """Test basic cytograph functionality"""
    print("🧠 Testing cytograph installation...")
    print(f"✅ cytograph version: {cytograph.__version__}")
    
    # Test importing main modules
    try:
        from cytograph import pipeline
        print("✅ pipeline module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import pipeline module: {e}")
        return False
    
    try:
        from cytograph import clustering
        print("✅ clustering module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import clustering module: {e}")
        return False
    
    try:
        from cytograph import embedding
        print("✅ embedding module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import embedding module: {e}")
        return False
    
    try:
        from cytograph import preprocessing
        print("✅ preprocessing module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import preprocessing module: {e}")
        return False
    
    # Test command line interface availability
    try:
        from cytograph.pipeline.commands import cli
        print("✅ CLI interface available")
    except ImportError as e:
        print(f"❌ Failed to import CLI interface: {e}")
        return False
    
    print("\n🎉 All tests passed! cytograph is ready to use.")
    return True

if __name__ == "__main__":
    success = test_cytograph()
    sys.exit(0 if success else 1)
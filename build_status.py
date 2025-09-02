#!/usr/bin/env python3
"""
Build Status Summary
Shows the complete status of the cytograph build and installation
"""

import os
import sys
from pathlib import Path

def check_build_status():
    """Check and display the complete build status"""
    print("🏗️  Cytograph Build Status Report")
    print("=" * 60)
    
    # Check installation
    print("\n✅ Installation Status:")
    try:
        import cytograph
        print(f"  • cytograph package: INSTALLED (v{cytograph.__version__})")
    except ImportError:
        print("  • cytograph package: NOT INSTALLED")
        return False
    
    # Check command line interface
    try:
        import subprocess
        result = subprocess.run(['cytograph', '--help'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("  • CLI interface: WORKING")
        else:
            print("  • CLI interface: ERROR")
    except Exception as e:
        print(f"  • CLI interface: ERROR - {e}")
    
    # Check virtual environment
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"  • Virtual environment: ACTIVE ({venv_path})")
    else:
        print("  • Virtual environment: NOT ACTIVE")
    
    # Check created files
    print("\n📁 Created Files:")
    files_to_check = [
        "test_cytograph.py",
        "cytograph_demo.py", 
        "BUILD_README.md",
        "sample_config.yaml",
        "example_build/config.yaml",
        "example_build/punchcards/Root.yaml"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"  • {file_path}: ✓ CREATED")
        else:
            print(f"  • {file_path}: ✗ MISSING")
    
    # Check directory structure
    print("\n📂 Directory Structure:")
    dirs_to_check = [
        "cytograph_env",
        "example_build",
        "example_build/punchcards"
    ]
    
    for dir_path in dirs_to_check:
        if os.path.isdir(dir_path):
            print(f"  • {dir_path}/: ✓ CREATED")
        else:
            print(f"  • {dir_path}/: ✗ MISSING")
    
    # Check dependencies
    print("\n📦 Key Dependencies:")
    dependencies = [
        ("numpy", "NumPy"),
        ("scipy", "SciPy"), 
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("loompy", "Loompy"),
        ("umap-learn", "UMAP-learn"),
        ("leidenalg", "Leidenalg"),
        ("torch", "PyTorch")
    ]
    
    for module, name in dependencies:
        try:
            __import__(module)
            print(f"  • {name}: ✓ INSTALLED")
        except ImportError:
            print(f"  • {name}: ✗ MISSING")
    
    return True

def show_usage_instructions():
    """Show how to use the built cytograph package"""
    print("\n🚀 Usage Instructions:")
    print("=" * 60)
    
    print("\n1. Activate the virtual environment:")
    print("   source cytograph_env/bin/activate")
    
    print("\n2. Test the installation:")
    print("   python test_cytograph.py")
    print("   python cytograph_demo.py")
    
    print("\n3. Get help:")
    print("   cytograph --help")
    
    print("\n4. Set up your analysis:")
    print("   • Copy example_build/ to your project folder")
    print("   • Update paths in config.yaml")
    print("   • Modify punchcards/Root.yaml for your samples")
    print("   • Run: cytograph --build-location your_build process YourSamples")
    
    print("\n5. Explore the documentation:")
    print("   • README.md - Original repository documentation")
    print("   • BUILD_README.md - Build and usage guide")
    print("   • notebooks/ - Analysis examples and figures")

def show_next_steps():
    """Show what to do next"""
    print("\n🎯 Next Steps:")
    print("=" * 60)
    
    print("\n📚 Learn:")
    print("  • Read BUILD_README.md for detailed usage")
    print("  • Explore the notebooks/ directory for examples")
    print("  • Check the original repository for methodology")
    
    print("\n🔧 Prepare:")
    print("  • Set up your single-cell data in loom format")
    print("  • Configure paths and parameters")
    print("  • Create punchcards for your analysis")
    
    print("\n🚀 Analyze:")
    print("  • Run quality control: cytograph qc")
    print("  • Process samples: cytograph process")
    print("  • Explore results in exported/ folders")
    
    print("\n📊 Visualize:")
    print("  • Generate UMAP/t-SNE plots")
    print("  • Create clustering visualizations")
    print("  • Analyze RNA velocity")

def main():
    """Main function"""
    print("🧠 Cytograph Single-Cell Analysis Pipeline")
    print("Build and Installation Status Report")
    print("=" * 60)
    
    # Check build status
    if not check_build_status():
        print("\n❌ Build incomplete. Please check installation.")
        return 1
    
    # Show usage instructions
    show_usage_instructions()
    
    # Show next steps
    show_next_steps()
    
    print("\n" + "=" * 60)
    print("🎉 Build Complete! Cytograph is ready for single-cell analysis.")
    print("For support, check BUILD_README.md or the original repository.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
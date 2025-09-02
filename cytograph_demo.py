#!/usr/bin/env python3
"""
Cytograph Demonstration Script
Shows how to use cytograph for single-cell RNA-seq analysis
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Import cytograph modules
import cytograph
from cytograph import pipeline, clustering, embedding, preprocessing, plotting

def demonstrate_cytograph():
    """Demonstrate cytograph functionality"""
    print("🧠 Cytograph Single-Cell Analysis Pipeline Demo")
    print("=" * 60)
    
    # Show available commands
    print("\n📋 Available cytograph commands:")
    print("  • build      - Build a new analysis")
    print("  • merge      - Merge multiple datasets")
    print("  • mkloom     - Create loom files")
    print("  • pool       - Pool multiple samples")
    print("  • process    - Process samples through the pipeline")
    print("  • qc         - Quality control")
    print("  • split      - Split datasets")
    print("  • subset     - Create subsets")
    
    # Show pipeline structure
    print("\n🔧 Pipeline Components:")
    print("  • preprocessing  - Data preprocessing and quality control")
    print("  • clustering    - Cell clustering algorithms")
    print("  • embedding     - Dimensionality reduction (UMAP, t-SNE)")
    print("  • manifold      - Manifold learning")
    print("  • enrichment    - Gene set enrichment analysis")
    print("  • annotation    - Cell type annotation")
    print("  • plotting      - Visualization tools")
    
    # Show configuration example
    print("\n⚙️  Configuration Example:")
    config_example = """
# Example ~/.cytograph configuration file
paths:
  samples: "/path/to/samples"
  autoannotation: "/path/to/auto-annotation"
  metadata: "/path/to/metadata.csv"

# Example build folder structure
build_folder/
├── punchcards/
│   └── Root.yaml
├── config.yaml
└── data/
    """
    print(config_example)
    
    # Show punchcard example
    print("\n🎴 Punchcard Example (Root.yaml):")
    punchcard_example = """
MySamples:
    include: [[sample1, sample2, sample3]]

Neurons:
    include: [[MySamples]]
    subset: "Clusters == 'Neurons'"

NonNeurons:
    include: [[MySamples]]
    subset: "Clusters != 'Neurons'"
    """
    print(punchcard_example)
    
    # Show usage example
    print("\n🚀 Usage Example:")
    usage_example = """
# Process samples through the pipeline
cytograph --build-location /path/to/build process MySamples

# This will run:
# 1. Data pooling and preprocessing
# 2. Quality control and filtering
# 3. Dimensionality reduction
# 4. Clustering
# 5. Visualization
# 6. Velocity inference
    """
    print(usage_example)
    
    # Show output structure
    print("\n📁 Output Structure:")
    output_structure = """
build_folder/
├── data/
│   ├── MySamples.loom          # Processed data
│   └── MySamples.agg.loom     # Aggregated data
├── exported/
│   └── MySamples/
│       ├── clustering/         # Clustering results
│       ├── embedding/          # UMAP, t-SNE plots
│       ├── velocity/           # Velocity analysis
│       └── qc/                 # Quality control plots
└── logs/                       # Analysis logs
    """
    print(output_structure)
    
    # Show key features
    print("\n✨ Key Features:")
    print("  • Automated pipeline from raw data to results")
    print("  • Built-in quality control and filtering")
    print("  • Advanced clustering algorithms (Leiden, Louvain)")
    print("  • Multiple embedding methods (UMAP, t-SNE, OpenTSNE)")
    print("  • RNA velocity analysis")
    print("  • Automated cell type annotation")
    print("  • Comprehensive visualization suite")
    print("  • Reproducible analysis with punchcards")
    
    print("\n🎉 Cytograph is ready for single-cell analysis!")
    print("For more information, see: https://github.com/linnarsson-lab/adult-human-brain")

def show_installation_info():
    """Show installation and environment information"""
    print("\n🔍 Environment Information:")
    print(f"  • Python version: {sys.version}")
    print(f"  • Cytograph version: {cytograph.__version__}")
    print(f"  • Virtual environment: {os.environ.get('VIRTUAL_ENV', 'Not activated')}")
    
    # Check available packages
    print("\n📦 Key Dependencies:")
    try:
        import numpy as np
        print(f"  • NumPy: {np.__version__}")
    except ImportError:
        print("  • NumPy: Not available")
    
    try:
        import scipy
        print(f"  • SciPy: {scipy.__version__}")
    except ImportError:
        print("  • SciPy: Not available")
    
    try:
        import pandas as pd
        print(f"  • Pandas: {pd.__version__}")
    except ImportError:
        print("  • Pandas: Not available")
    
    try:
        import matplotlib
        print(f"  • Matplotlib: {matplotlib.__version__}")
    except ImportError:
        print("  • Matplotlib: Not available")

def create_sample_config():
    """Create a sample configuration file"""
    config_content = """# Sample cytograph configuration
# Save this as ~/.cytograph or in your build folder as config.yaml

paths:
  samples: "/path/to/your/samples"
  autoannotation: "/path/to/auto-annotation"
  metadata: "/path/to/metadata.csv"

# Analysis parameters
clustering:
  resolution: 0.5
  algorithm: "leiden"

embedding:
  method: "umap"
  n_neighbors: 15
  min_dist: 0.1

qc:
  min_genes: 200
  max_genes: 6000
  min_umis: 500
  max_mito: 0.2
"""
    
    with open("sample_config.yaml", "w") as f:
        f.write(config_content)
    
    print("\n📝 Sample configuration file created: sample_config.yaml")
    print("   Customize this file for your analysis needs.")

def main():
    """Main demonstration function"""
    try:
        demonstrate_cytograph()
        show_installation_info()
        create_sample_config()
        
        print("\n" + "=" * 60)
        print("🎯 Next Steps:")
        print("1. Set up your sample data in loom format")
        print("2. Configure paths in ~/.cytograph or config.yaml")
        print("3. Create punchcards for your analysis")
        print("4. Run: cytograph --build-location /path/to/build process YourSamples")
        print("5. Explore results in the exported/ folder")
        
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
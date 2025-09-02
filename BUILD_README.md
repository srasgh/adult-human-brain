# Cytograph Build and Installation Guide

This repository contains the **cytograph** package, a comprehensive pipeline for single-cell RNA-seq analysis developed by the Linnarsson Lab.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+ (tested with Python 3.13.3)
- pip package manager
- Virtual environment support (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/linnarsson-lab/adult-human-brain.git
   cd adult-human-brain
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv cytograph_env
   source cytograph_env/bin/activate
   ```

3. **Install cytograph:**
   ```bash
   pip install --upgrade pip
   pip install -e .
   ```

4. **Verify installation:**
   ```bash
   cytograph --help
   python -c "import cytograph; print(cytograph.__version__)"
   ```

## 🧠 What is Cytograph?

Cytograph is an automated pipeline for single-cell RNA-seq analysis that provides:

- **End-to-end analysis** from raw data to publication-ready results
- **Standardized workflow** with built-in quality control
- **Advanced algorithms** for clustering, embedding, and velocity analysis
- **Reproducible research** through punchcard-based configuration
- **Comprehensive visualization** suite for exploration and publication

## 📋 Available Commands

```bash
cytograph build      # Build a new analysis
cytograph merge      # Merge multiple datasets
cytograph mkloom     # Create loom files
cytograph pool       # Pool multiple samples
cytograph process    # Process samples through the pipeline
cytograph qc         # Quality control
cytograph split      # Split datasets
cytograph subset     # Create subsets
```

## ⚙️ Configuration

### Global Configuration (~/.cytograph)
```yaml
paths:
  samples: "/path/to/your/samples"
  autoannotation: "/path/to/auto-annotation"
  metadata: "/path/to/metadata.csv"
```

### Build-Specific Configuration (config.yaml)
```yaml
paths:
  autoannotation: "/path/to/specific/auto-annotation"

clustering:
  resolution: 0.5
  algorithm: "leiden"

embedding:
  method: "umap"
  n_neighbors: 15
  min_dist: 0.1
```

## 🎴 Punchcards

Punchcards define how samples are combined and analyzed. Create `punchcards/Root.yaml`:

```yaml
MySamples:
    include: [[sample1, sample2, sample3]]

Neurons:
    include: [[MySamples]]
    subset: "Clusters == 'Neurons'"

NonNeurons:
    include: [[MySamples]]
    subset: "Clusters != 'Neurons'"
```

## 🚀 Running Analysis

### Basic Usage
```bash
# Process samples through the pipeline
cytograph --build-location /path/to/build process MySamples
```

### Complete Workflow
1. **Set up build folder:**
   ```
   build_folder/
   ├── punchcards/
   │   └── Root.yaml
   ├── config.yaml
   └── data/
   ```

2. **Run analysis:**
   ```bash
   cytograph --build-location build_folder process MySamples
   ```

3. **Explore results:**
   ```
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
   ```

## 🔧 Pipeline Components

The cytograph pipeline includes:

- **Preprocessing**: Quality control, filtering, normalization
- **Clustering**: Leiden, Louvain, and other algorithms
- **Embedding**: UMAP, t-SNE, OpenTSNE dimensionality reduction
- **Manifold Learning**: Advanced manifold learning techniques
- **Enrichment**: Gene set enrichment analysis
- **Annotation**: Automated cell type annotation
- **Visualization**: Comprehensive plotting and exploration tools

## 📊 Data Formats

### Input
- **Loom files** (`.loom`) - Single-cell data in loom format
- **Metadata** - Sample information in CSV format
- **Auto-annotations** - Pre-trained cell type annotations

### Output
- **Processed data** - Quality-controlled and normalized data
- **Clustering results** - Cell cluster assignments
- **Embeddings** - Dimensionality reduction coordinates
- **Visualizations** - Publication-ready plots
- **Velocity analysis** - RNA velocity results

## 🧪 Testing

Run the test suite to verify installation:

```bash
python test_cytograph.py
python cytograph_demo.py
```

## 📚 Documentation

- **Repository**: https://github.com/linnarsson-lab/adult-human-brain
- **Paper**: Siletti et al. (2022) - Single-cell analysis of the adult human brain
- **Dataset**: 3,369,219 cells available for download
- **Browser**: CELLxGENE collection for interactive exploration

## 🔍 Troubleshooting

### Common Issues

1. **Python version compatibility**: Ensure Python 3.9+
2. **Virtual environment**: Always activate before use
3. **Dependencies**: Check all required packages are installed
4. **Configuration**: Verify paths in config files

### Getting Help

- Check the cytograph help: `cytograph --help`
- Review the sample configuration: `sample_config.yaml`
- Explore the notebooks in `notebooks/` directory
- Check the original repository for detailed documentation

## 🎯 Next Steps

1. **Set up your data** in loom format
2. **Configure paths** in `~/.cytograph` or `config.yaml`
3. **Create punchcards** for your analysis
4. **Run the pipeline**: `cytograph --build-location /path/to/build process YourSamples`
5. **Explore results** in the exported folder

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Linnarsson Lab** - Development and maintenance
- **Siletti et al.** - Original research and methodology
- **Single-cell community** - Contributions and feedback

---

**Happy analyzing! 🧠✨**
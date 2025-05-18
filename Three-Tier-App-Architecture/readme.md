# Architecture Diagrams with Python

This repository contains Python scripts to generate architecture diagrams using the `diagrams` library.

## Prerequisites

- Python 3.6 or higher
- Graphviz (required by the diagrams library)

## Installation

1. Install Graphviz:
   - macOS: `brew install graphviz`
   - Ubuntu/Debian: `sudo apt-get install graphviz`
   - Windows: Download from [Graphviz website](https://graphviz.org/download/)

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Available Diagrams

### Three-Tier Web Application

A traditional three-tier architecture with web, application, and data tiers.

```
python three_tier_architecture.py
```

This will generate `three-tier-web-application.png` in the current directory.

### Microservices Architecture

A modern microservices architecture with API Gateway, various services, and databases.

```
python microservices_architecture.py
```

This will generate `microservices-architecture.png` in the current directory.

## Creating Your Own Diagrams

You can modify the existing scripts or create new ones based on your specific architecture needs. The `diagrams` library supports various cloud providers including AWS, Azure, GCP, and more.

## Documentation

For more information on the diagrams library, visit:
https://diagrams.mingrammer.com/
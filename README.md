# ship-vessel-intelligence-platform


## Project Overview

Production-grade data pipeline processing 50M+ maritime vessel tracking records using medallion architecture (Bronze/Silver/Gold layers).

**Timeline:** September - October 2026  
**Expected Data Volume:** 50M-100M+ records  
**Architecture:** Medallion (Delta Lake)

## Quick Start

### Prerequisites
- Python 3.8+
- PySpark 3.3+
- Databricks workspace (or local Spark)
- Azure/AWS cloud account
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/[YOUR-USERNAME]/vessel-intelligence-platform.git
cd vessel-intelligence-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp config/.env.example config/.env
# Edit config/.env with your credentials
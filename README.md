# media-immersion

A Python project for analyzing themes related to viewer immersion in media. Custom dataset curated from [TMDB](https://developer.themoviedb.org/).

## Setup

Clone the repository:
```bash
git clone https://github.com/harrisonfloam/media-immersion.git
```

Activate the development environment:
```bash
conda env create -f environment.yml
conda activate media-immersion
pip install -e .
```

<!-- 
Update the environment if any packages are added:

###### MacOS
```bash
conda env export --no-builds | grep -v '^prefix:' > environment.yml
```

###### Windows
```powershell
conda env export --no-builds | Select-String -NotMatch '^prefix:' | Out-File -Encoding utf8 environment.yml
```

## Dependencies

The only external dependency is [Ollama](https://ollama.com/download/windows), required for prediction with a locally installed LLM.
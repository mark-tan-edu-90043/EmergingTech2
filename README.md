# FastAPI Application

This is a FastAPI application that demonstrates basic usage.

Uses https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0

Can otherwise use https://huggingface.co/runwayml/stable-diffusion-v1-5 for better performance/load times, but worse image generation.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/mark-tan-edu-90043/EmergingTech2.git
cd EmergingTech2

```

### 2. Install all dependencies using either of the following:

pip install -r requirements.txt

or

pip3 install -r requirements.txt

or if everything fails

pip3 install -r requirements.txt --user

### 3. Run the application using

python -m uvicorn app.main:app --reload

### 4. Use application in browser

visit http://localhost:8000

### 5. Generate a cool image

Loading times may vary

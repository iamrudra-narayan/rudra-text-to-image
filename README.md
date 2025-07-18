# FastAPI Image Generation API

This FastAPI application provides two endpoints to interact with the Piclumen image generation API:

* `/generate-image`: Trigger image generation with custom prompts and parameters.
* `/check-image`: Check the status and get the generated image URL.

---

## Features

* Fully customizable payload with sensible defaults.
* Async HTTP calls using `httpx`.
* User-provided Authorization Token via query params.
* Suitable for frontend or automated backend integration.

---

## API Endpoints

### 1. `POST /generate-image`

Initiate image generation.

**Query Parameters:**

* `authorization_token`: (string, required)

**Body Parameters (JSON):**

```json
{
  "prompt": "a magical landscape",
  "highPixels": false,
  "model_id": "23887bba-507e-4249-a0e3-6951e4027f2b",
  "negative_prompt": "",
  "resolution": {
    "width": 1344,
    "height": 768,
    "batch_size": 1
  },
  "model_ability": {},
  "seed": 9896923949,
  "steps": 6,
  "cfg": 1,
  "sampler_name": "euler",
  "scheduler": "normal",
  "ponyTags": {},
  "denoise": 1,
  "hires_fix_denoise": 0.5,
  "hires_scale": 2,
  "multi_img2img_info": {
    "style_list": []
  },
  "img_control_info": {
    "style_list": []
  },
  "continueCreate": false
}
```

**Response:**

```json
{
  "statuscode": 200,
  "message": "Image creation initiated",
  "mark_id": "abc123"
}
```

---

### 2. `POST /check-image`

Check image status and retrieve URL.

**Query Parameters:**

* `authorization_token`: (string, required)
* `mark_id`: (string, required)

**Response (if ready):**

```json
{
  "statuscode": 200,
  "message": "Image generation successful",
  "image_url": "https://..."
}
```

**Response (if still processing):**

```json
{
  "statuscode": 202,
  "message": "Image still processing. Current status: pending",
  "mark_id": "abc123"
}
```

---

## Local Development

### 🧪 Requirements

```bash
pip install fastapi uvicorn httpx
```

### 🚀 Run Locally

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access Swagger UI.

---

## 🌐 Deployment on Render.com

### 1. Create GitHub Repository

Push the FastAPI code (including `main.py`, `requirements.txt`, `README.md`) to a GitHub repo.

### 2. Add `requirements.txt`

```txt
fastapi
uvicorn
httpx
```

### 3. Create `render.yaml` (Optional)

```yaml
services:
  - type: web
    name: fastapi-image-api
    runtime: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port 10000"
    envVars:
      - key: PORT
        value: 10000
```

### 4. Deploy on Render

* Go to [https://render.com](https://render.com)
* Click **"New Web Service"** > **"Deploy from GitHub"**
* Choose repo > Select runtime = **Python**
* Set **Start Command:**

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```
* Set **Build Command:**

  ```bash
  pip install -r requirements.txt
  ```
* Deploy 🎉

---

## 🛡️ Notes

* Token is passed as query param to keep Swagger UI simple.
* For production, consider using `Authorization` header with `Depends`.

---

## 🧠 Credits

Built with FastAPI and Render.com by Rudra.

---

For help or issues, feel free to raise an issue on the GitHub repo or contact me.
Email Id: agentic.rudra@gmail.com

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🧠 For Your Self, Please Flow this
**TextToImage API using FastAPI: End-to-End Setup, Deployment, and Testing Guide**

---

## 🌟 Project Title:

**TextToImage API (Built with FastAPI)**

## 📄 Summary:

This project allows you to send a text prompt and get back an AI-generated image using a public free API (no API key required). It's built using FastAPI and deployed on Render.

---

## 🚀 Features:

* Text to image generation using a free model (e.g., HuggingFace model like `stabilityai/stable-diffusion-2`)
* POST API to send text and get image URL in response
* Swagger UI (auto-generated docs)
* Easily deployable to Render

---

## 📚 Technologies Used:

* Python 3.10+
* FastAPI
* Uvicorn
* Requests
* Render (deployment)
* GitHub (version control)

---

## 📂 Project Structure:

```
TextToImage-API/
├── main.py               # FastAPI app file
├── requirements.txt      # Dependencies
└── README.md             # Documentation (this file)
```

---

## ✅ Setup Guide (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/iamrudra-narayan/rudra-text-to-image.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

### 4. Access the API Docs

Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to test the API.

---

## 📆 GitHub Repository Setup (from Scratch)

### 1. Create GitHub Account

* Visit: [https://github.com](https://github.com)
* Sign up with email or Gmail
* Verify and login

### 2. Create New Repository

* Click on **New** > Name it: `TextToImageApi`
* Keep it Public, do not initialize with README

### 3. Initialize Git & Push Code

```bash
# Inside your project directory
git init
git checkout -b master

git add .
git commit -m "Initial commit"
git remote add origin https://github.com/iamrudra-narayan/rudra-text-to-image.git
git push -u origin master
```

---

## 🌐 Deployment Guide (Render)

### 1. Push Code to GitHub

(Use the steps above)

### 2. Create a Web Service on Render

* Go to [https://render.com](https://render.com)
* Click **New Web Service**
* Connect your GitHub repo
* Select branch and set build & start commands

### 3. Set Render Configuration:

* **Build Command**: *(leave empty)*
* **Start Command**:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

* **Instance Type**: Free

### 4. Deploy

Click **Create Web Service**. Render will build and host your API.

### 5. Test Deployed API

Visit `https://your-app-name.onrender.com/docs` and test your API live.

---

## 👀 Sample API Usage

### Endpoint 1:

`POST /generate-image`

**Description**: Generate a new image based on a given text prompt.

#### ✅ Request Body (JSON):
Authorization_Key : "8c0061b6c4ee7b67f1397444313f70dc259a3b5c"
```json
{
    "highPixels": false,
    "model_id": "23887bba-507e-4249-a0e3-6951e4027f2b",
    "prompt": "A man selfie with a lion in jungle",
    "negative_prompt": "",
    "resolution": {
        "width": 1344,
        "height": 768,
        "batch_size": 1
    },
    "model_ability": {},
    "seed": 9896923949,
    "steps": 6,
    "cfg": 1,
    "sampler_name": "euler",
    "scheduler": "normal",
    "ponyTags": {},
    "denoise": 1,
    "hires_fix_denoise": 0.5,
    "hires_scale": 2,
    "multi_img2img_info": {
        "style_list": []
    },
    "img_control_info": {
        "style_list": []
    },
    "continueCreate": false
}
```

#### 🔁 Response:

```json
{
    "status": 0,
    "message": "success",
    "data": {
        "markId": "dca0d07b-41f8-41ec-8b68-0bcb3a843dc4",
        "featureName": "ttp",
        "fastHour": true,
        "index": -1
    }
}
```

#### 🧪 CURL Example:

```bash
curl -X 'POST' \
  'https://your-app-name.onrender.com/generate-image' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "A cyberpunk city at night"
}'
```

---

### Endpoint 2:

`GET check-image /`

**Description**: Base route that returns a simple HTML or welcome message (optional).

#### 🔁 Request:
```json
Authorization Key: 8c0061b6c4ee7b67f1397444313f70dc259a3b5c
mark_id: "03debf7f-9f34-431c-8f94-166ab1bb4f70"
```

#### 🔁 Response:
```json

```json

```

#### 🧪 CURL Example:

```bash
curl https://your-app-name.onrender.com/
```

---

## 🔗 Useful Links

* FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
* Render: [https://render.com/](https://render.com/)
* GitHub: [https://github.com/](https://github.com/)

---

## 🎥 Ready-to-Use Commands

```bash
# Clone project
git clone https://github.com/yourusername/TextToImage-API.git

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload

# GitHub upload setup
git init
git checkout -b master
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/TextToImage-API.git
git push -u origin master

# Start command for Render
uvicorn main:app --host 0.0.0.0 --port 10000
```


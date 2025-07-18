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

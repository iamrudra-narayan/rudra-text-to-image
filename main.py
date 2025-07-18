from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import httpx
from typing import Optional, List, Dict, Any

app = FastAPI()


class Resolution(BaseModel):
    width: int
    height: int
    batch_size: int


class ImageRequest(BaseModel):
    prompt: str
    highPixels: bool = False
    model_id: str = "23887bba-507e-4249-a0e3-6951e4027f2b"
    negative_prompt: str = ""
    resolution: Resolution = Resolution(width=1344, height=768, batch_size=1)
    model_ability: Dict[str, Any] = {}
    seed: int = 9896923949
    steps: int = 6
    cfg: int = 1
    sampler_name: str = "euler"
    scheduler: str = "normal"
    ponyTags: Dict[str, Any] = {}
    denoise: float = 1
    hires_fix_denoise: float = 0.5
    hires_scale: int = 2
    multi_img2img_info: Dict[str, Any] = {"style_list": []}
    img_control_info: Dict[str, Any] = {"style_list": []}
    continueCreate: bool = False


class CheckImageRequest(BaseModel):
    mark_id: str


@app.post("/generate-image")
async def generate_image(
    request: ImageRequest,
    authorization_token: str = Query(..., description="Authorization token")
):
    headers = {
        "accept": "application/json",
        "authorization": authorization_token,
        "content-type": "application/json;charset=UTF-8",
        "platform": "Web",
        "origin": "https://piclumen.com",
        "referer": "https://piclumen.com/",
        "user-agent": "Mozilla/5.0"
    }

    payload = request.dict()

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            "https://api.piclumen.com/api/gen/create",
            headers=headers,
            json=payload
        )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    mark_id = response.json()["data"]["markId"]

    return {
        "statuscode": 200,
        "message": "Image creation initiated",
        "mark_id": mark_id
    }


@app.post("/check-image")
async def check_image(
    mark_id: str = Query(..., description="Mark ID to check image status"), 
    authorization_token: str = Query(..., description="Authorization token")
):
    headers = {
        "accept": "application/json",
        "authorization": authorization_token,
        "content-type": "application/json;charset=UTF-8",
        "platform": "Web",
        "origin": "https://piclumen.com",
        "referer": "https://piclumen.com/",
        "user-agent": "Mozilla/5.0"
    }

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            check_res = await client.post(
                "https://api.piclumen.com/api/task/batch-process-task",
                headers=headers,
                json=[mark_id]
            )

        if check_res.status_code != 200:
            raise HTTPException(status_code=check_res.status_code, detail=check_res.text)

        check_data = check_res.json()["data"][0]
        status = check_data["status"]

        if status != "success":
            return {
                "statuscode": 202,
                "message": f"Image still processing. Current status: {status}",
                "mark_id": mark_id
            }

        image_url = check_data["img_urls"][0]["imgUrl"]

        return {
            "statuscode": 200,
            "message": "Image generation successful",
            "image_url": image_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
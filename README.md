# Stable diffusion API 📚🔎
![version](https://img.shields.io/badge/version-0.0.3-blue)
![python](https://img.shields.io/badge/python-3.8.7-brightgreen)

### Local installation ###

To prepare the project, the following steps will be necessary:
> - Install [git](https://git-scm.com/downloads) locally;
> - On your local server, run a `git clone` command;

### Local execution ###
To execute the project, there's two ways to do it:
> - First download [python 3](https://www.python.org/). After, install the dependencies by typing `pip install -r requirements.txt` and run `python main.py` on your terminal if you just want to verify all the routes and see if the API algorithm is working;
> - If you already have Docker installed on you machine, run `docker-compose -f docker-compose.dev.yml up --build -d` on the terminal to create an image and container for the aplication (and for the cache server when it's available). This way allows you to install all application dependencies as well as automate the API testing process through docker;

> **In both flows, after uploading the application you can access it at localhost:8000/docs, as well as check the logs informations at localhost:8000/stable-diffusion/logs**.

### Feature ###

The repository features the following tool:
> - This repository contains a tool in REST API format to generate images using the public stable diffusion model trained by the hugging face company 🤗.
  
### Routes ### 

#### ***AI image generator*** 
  * POST `/stable-diffusion/image`
  * Request body
  ```ts
  {
  "text": "string"
  }
  ```

  * Media type: `application/json`
  * Response
  ```ts
  {
  "image": '_filename'.jpg
  }
  ```

#### ***Metrics***
  * GET `/stable-diffusion/metrics`
  * Media type: `text/plain`
  * Response
  ```ts
  "string"
  ```

#### ***Logs***
  * GET `/stable-diffusion/logs`
  * Media type: `text/plain`
  * Response
  ```ts
  "string"
  ```

#### ***Health*** 
  * GET `/stable-diffusion/health`
  * Media type: `application/json`
  * Response
  ```ts
  {
  "health": "string"
  }
  ```

* * *

## Example of use:

After asking for a specific word, the API will return a AI created image related to the respective requested word, as shown in the following examples:

### Image

POST `http://localhost:8000/stable-diffusion/image`

Request Body: 
```ts
  {
  "text": "A realistic image of Synthwave futuristic city"
  }
```
Response Body:

![image1](samples/A_realistic_image_of_Synthwave_futuristic_city.png)

---

Request Body: 
```ts
  {
  "text": "impressionist painting of a galaxy"
  }
```
Response Body:

![image2](samples/impressionist_painting_of_a_galaxy.png)

### Project Technologies ###

* FastAPI
* Prometheus
* Graypy
* Diffusers
* Transformers
* StableDiffusion
* Redis

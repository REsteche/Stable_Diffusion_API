# Stable diffusion API 📚🔎
![version](https://img.shields.io/badge/version-0.0.1-blue)
![python](https://img.shields.io/badge/python-3.8.7-brightgreen)

### Local installation ###

To prepare the project, the following steps will be necessary:
> - Install [python 3](https://www.python.org/) and [git](https://git-scm.com/downloads);
> - On your local server, run a `git clone` command;
> - Download the requirements.txt file with the project dependencies by typing `pip install -r requirements.txt` (it is strongly recommended that you do it within a virtual environment .env to avoid version conflict with other packages in your base installation.).

### To run it locally ###
There are two ways to run the application locally, 
> - Open a cmd prompt inside the directory where you installed the application, and access your virtual environment (recommended) or your (base:) environment and run the command `python main.py`.
> - Install docker on your machine through [Link](https://docs.docker.com/get-docker/), open a cmd inside your aplication directory and run `docker-compose -f docker-compose.dev.yml up --build -d` to create both the image and container for your aplication. 


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

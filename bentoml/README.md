## Train Model
```shell
python main.py
```
## Creating a Service
```shell
# deploy
bentoml serve service:svc --reload

# request
curl \
  -X POST \
  -H "content-type: application/json" \
  --data "[[5.9, 3, 5.1, 1.8]]" \
  http://127.0.0.1:3000/classify

# bentoml build & serve
bentoml build
bentoml serve iris_classifier:latest --production

# docker build & deploy
bentoml containerize iris_classifier:latest
docker run -p 3000:3000 iris_classifier:6otbsmxzq6lwbgx
```
## Reference
[BentoML](https://docs.bentoml.org/en/latest/tutorial.html)
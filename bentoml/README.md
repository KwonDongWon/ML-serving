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
```
## Reference
[BentoML](https://docs.bentoml.org/en/latest/tutorial.html)
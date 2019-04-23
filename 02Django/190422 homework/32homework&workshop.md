# 32homework

1. `JSON`, `YAML`
2. `python manage.py loaddata <fixturename>`



# 32workshop

`myapp/fixtures` 디렉토리 내에 다음과 같은 json 파일을 만든다.

### musician.json

```json
[
    {
      "model": "myapp.musician",
      "pk": 1,
      "fields": {
        "first_name": "John",
        "last_name": "Lennon"
      }
    },
    {
      "model": "myapp.musician",
      "pk": 2,
      "fields": {
        "first_name": "Paul",
        "last_name": "McCartney"
      }
    }
  ]
```

다음 명령으로 통해 데이터베이스에 반영한다.

`$ python manage.py loaddata musician.json`


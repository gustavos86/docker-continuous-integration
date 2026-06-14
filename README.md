# Unit test

```
python -m pytest -v web/test/unit/
```

# Integration test

```
python -m pytest -v web/test/integration/
```

# e2e test

```
python -m pytest -v web/test/e2e/ \
  --flask-url http://127.0.0.1:5000 \
  --redis-url redis://127.0.0.1:6379
```

# Start app

```
docker start redis-server
flask --app page_tracker.app run
```

# black

```
python -m black src/ --check
```

# isort

```
python -m isort web/src/
```

# flake8

```
python -m flake8 web/src/
```

# pylint

```
python -m pylint web/src/
```

# bandit

```
python -m bandit -r web/src/ --quiet
```

# docker

```
docker build -t page-tracker .
docker build -f Dockerfile.dev -t page-tracker .
```

```
$ git rev-parse --short HEAD
docker build -t page-tracker:$(git rev-parse --short HEAD) .
```


# Run Container

```
docker run -p 80:5000 --name web-service gustavos86/page-tracker 
```

```
docker run -d \
             -v redis-volume:/data \
             --network page-tracker-network \
             --name redis-service \
             redis:7.0.10-bullseye
```

```
docker run -d \
             -p 80:5000 \
             -e REDIS_URL=redis://redis-service:6379 \
             --network page-tracker-network \
             --name web-service \
             gustavos86/page-tracker 
```

```
docker compose up -d
docker compose ps
docker compose logs --follow
docker compose stop
docker compose restart
docker compose down --volumes
```

You have to tell Docker Compose to rebuild your image. You can do so with either of the following commands:

```
docker compose build
docker compose up --build
```

# end-to-end test

```
python -m pytest web/test/e2e/ \
  --flask-url http://localhost \
  --redis-url redis://localhost:6379
```

# Pause/unpause

```
docker compose pause
docker compose unpause
```

# Container end-to-end test

```
docker compose --profile testing up -d
docker compose ps -a
docker compose logs test-service
```
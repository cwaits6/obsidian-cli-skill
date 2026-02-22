---
type: concept
context: work
topic: devops
created: 2024-02-09
---

# Docker Basics

Containers package applications with their dependencies for consistent deployment.

## Key Concepts

- **Image** — a blueprint (like a class)
- **Container** — a running instance (like an object)
- **Dockerfile** — instructions to build an image
- **Volume** — persistent storage outside the container
- **Network** — communication between containers

## Common Commands

```bash
docker build -t myapp .
docker run -p 8080:80 myapp
docker ps                    # list running containers
docker logs <container>      # view logs
docker exec -it <container> sh  # shell into container
```

## Best Practices

1. Use multi-stage builds to keep images small
2. Don't run as root inside containers
3. Pin base image versions
4. Use `.dockerignore` to exclude unnecessary files

Related to [[Projects/Automation]] — the CLI could be containerized for CI/CD.

Quick ref for Helm values override patterns

## Inline Override

```bash
helm install myapp ./chart --set image.tag=v1.2.3
```

## Multiple Values

```bash
helm install myapp ./chart \
  --set image.tag=v1.2.3 \
  --set replicaCount=3 \
  --set service.type=LoadBalancer
```

## Values File

```bash
helm install myapp ./chart -f production-values.yaml
```

## Precedence (last wins)

```bash
helm install myapp ./chart \
  -f base-values.yaml \
  -f env-values.yaml \
  --set image.tag=v1.2.3
```

Order: chart defaults < base-values.yaml < env-values.yaml < --set flags

## Nested Keys

```bash
helm install myapp ./chart --set ingress.hosts[0].host=app.example.com
```

## JSON Strings

```bash
helm install myapp ./chart --set-json 'resources={"limits":{"cpu":"500m","memory":"256Mi"}}'
```

---
type: troubleshooting
context: work
topic: "[kubernetes]"
resolved: true
---
# K8s Pod Stuck in Pending

Had a pod stuck in Pending for 20 minutes today. Here's what I found.

## Symptoms

- `kubectl get pods` shows STATUS = Pending
- No events from the scheduler
- Other pods in the namespace are running fine

## Root Cause

The node pool was at capacity. The pod requested 4Gi memory but the largest available slot was 2Gi.

## Fix

Scaled up the node pool:
```
gcloud container clusters resize my-cluster --node-pool default-pool --num-nodes 5
```

Also worth checking:
- `kubectl describe pod <name>` — look for FailedScheduling events
- Resource requests vs node allocatable
- Node taints and tolerations
- PVC binding issues if volumes are involved

## Lessons Learned

Always set resource requests conservatively. We were requesting 4Gi when the app only used 1.5Gi at peak. Dropped to 2Gi and it scheduled immediately.

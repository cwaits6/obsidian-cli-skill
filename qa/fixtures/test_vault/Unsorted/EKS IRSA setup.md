# EKS IRSA Setup

Steps to configure IAM Roles for Service Accounts on EKS so pods can assume IAM roles without node-level permissions.

## Step 1: Enable OIDC Provider

```bash
eksctl utils associate-iam-oidc-provider \
  --cluster my-cluster \
  --approve
```

Verify:
```bash
aws eks describe-cluster --name my-cluster \
  --query "cluster.identity.oidc.issuer" --output text
```

## Step 2: Create IAM Policy

Create a policy with the minimum permissions your app needs:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

## Step 3: Create IAM Role with Trust Policy

```bash
eksctl create iamserviceaccount \
  --name my-app-sa \
  --namespace default \
  --cluster my-cluster \
  --attach-policy-arn arn:aws:iam::123456789:policy/my-app-policy \
  --approve
```

## Step 4: Annotate the Service Account

If not using eksctl, manually annotate:
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-app-sa
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/my-app-role
```

## Step 5: Update Pod Spec

Reference the service account in your deployment:
```yaml
spec:
  serviceAccountName: my-app-sa
```

## Verification

Check that the pod has AWS credentials injected:
```bash
kubectl exec -it my-pod -- env | grep AWS
```

You should see `AWS_ROLE_ARN` and `AWS_WEB_IDENTITY_TOKEN_FILE`.

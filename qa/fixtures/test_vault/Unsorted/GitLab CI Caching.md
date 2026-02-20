# Setting Up Caching in GitLab CI

Pipeline was taking 12 minutes because it re-downloaded all dependencies every run. Here's how I added caching.

## Step 1: Identify Cacheable Directories

For a Node.js project:
- `node_modules/` — npm packages
- `.npm/` — npm cache directory

For Python:
- `.pip-cache/` — pip downloads
- `.venv/` — virtual environment

## Step 2: Add Cache Config to .gitlab-ci.yml

```yaml
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.pip-cache"

cache:
  key:
    files:
      - requirements.txt
  paths:
    - .pip-cache/
    - .venv/
```

Using `files` in the cache key means the cache invalidates when requirements.txt changes.

## Step 3: Per-Job Cache Overrides

Some jobs need different cache settings:

```yaml
test:
  cache:
    key: test-$CI_COMMIT_REF_SLUG
    paths:
      - .pip-cache/
    policy: pull
```

`policy: pull` means this job reads the cache but never writes to it. Saves upload time.

## Step 4: Verify

Check the job logs for "Restoring cache" and "Saving cache" messages. First run will be slow (cache miss), subsequent runs should be faster.

## Results

Pipeline went from 12 minutes to 4 minutes. The cache upload adds ~20 seconds but saves 8 minutes of downloads.

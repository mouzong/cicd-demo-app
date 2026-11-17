# GitOps Platform Engineering Demo

[![CI](https://github.com/mouzong/cicd-demo-app/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mouzong/cicd-demo-app/actions/workflows/ci.yml)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![GitOps with Argo CD](https://img.shields.io/badge/GitOps-Argo%20CD-EF7B4D?style=flat&logo=argo&logoColor=white)](https://argo-cd.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


A small Python Flask app that returns a greeting at `GET /` on port `8080`.
This project demonstrates how to containerize an app, run CI with GitHub Actions,
and deploy it to Kubernetes using manifests that a GitOps controller can sync.

## Repository layout

| Path | Purpose |
| --- | --- |
| `app/app.py` | Flask app and hello endpoint |
| `Dockerfile` | Container image definition |
| `.github/workflows/ci.yml` | GitHub Actions CI workflow |
| `deploy/deployment.yaml` | Kubernetes Deployment |
| `deploy/service.yaml` | Kubernetes Service |

## Run locally

```bash
docker build -t cicd-demo-app .
docker run --rm -p 8080:8080 cicd-demo-app
```

In another terminal, run `curl http://localhost:8080/`. The app listens on
`0.0.0.0:8080` inside the container. With port `8080` published, another
machine can reach `http://<docker-host-ip>:8080/` if the network and firewall allow it.

## Deploy to Kubernetes

Set the image in `deploy/deployment.yaml` to a tag your cluster can pull, then apply the manifests.

```bash
kubectl create ns cicd-demo-app
kubectl apply -n cicd-demo-app -f deploy/
kubectl get deployments,pods,services
```

To test the endpoint from your machine, replace `<service-name>` and
`<service-port>` with the name and port defined in `deploy/service.yaml`.

```bash
kubectl port-forward svc/<service-name> 8080:<service-port>
curl http://localhost:8080/
```

For a GitOps deployment, point your controller at the `deploy/` directory.
Commit manifest changes to Git and let the controller reconcile the cluster.

## License

This project is licensed under the [MIT License](LICENSE).

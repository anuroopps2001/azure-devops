```bash
helm create blob-app
```

```bash
azureuser@agent-vm:~/azure-devops$ tree blob-app/
blob-app/
├── Chart.yaml
├── charts
├── templates
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── httproute.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   ├── serviceaccount.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

3 directories, 11 files
```


### Clean default templates

Delete everything inside `templates` directory


### Create deployment.yaml in templates dir and update values.yaml
templates/deployment.yaml:
```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: blob-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: blob-app
  template:
    metadata:
      labels:
        app: blob-app
        azure.workload.identity/use: "true"
    spec:
      serviceAccountName: storage-sa
      containers:
        - name: app
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 80
```

values.yaml:
```bash
image:
  repository: anuroopacr12345.azurecr.io/python-azure-storage
  tag: latest
```

### Install helm chart
```bash
azureuser@agent-vm:~/azure-devops/helm-chart$ helm install blob-app ./blob-app
NAME: blob-app
LAST DEPLOYED: Mon May  4 05:23:46 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
TEST SUITE: None
azureuser@agent-vm:~/azure-devops/helm-chart$ helm ls
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
blob-app        default         1               2026-05-04 05:23:46.099754422 +0000 UTC deployed        blob-app-0.1.0  1.16.0
azureuser@agent-vm:~/azure-devops/helm-chart$ kubectl get pods
NAME                        READY   STATUS             RESTARTS     AGE
blob-app-5755946f4b-5ff6s   0/1     Completed          1 (5s ago)   8s
azureuser@agent-vm:~/azure-devops/helm-chart$
```

### Upgrade
```bash
helm upgrade blob-app ./blob-app \
  --set image.tag=<new-tag>
```

```bash
azureuser@agent-vm:~/azure-devops/helm-chart$ helm upgrade blob-app ./blob-app --set image.tag=19
Release "blob-app" has been upgraded. Happy Helming!
NAME: blob-app
LAST DEPLOYED: Mon May  4 05:25:12 2026
NAMESPACE: default
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete
TEST SUITE: None
azureuser@agent-vm:~/azure-devops/helm-chart$ helm ls
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
blob-app        default         2               2026-05-04 05:25:12.006685855 +0000 UTC deployed        blob-app-0.1.0  1.16.0
azureuser@agent-vm:~/azure-devops/helm-chart$ kubectl get pods
NAME                        READY   STATUS      RESTARTS      AGE
blob-app-5db5dd74c5-glhs4   0/1     Completed   1 (11s ago)   12s
azureuser@agent-vm:~/azure-devops/helm-chart$
```

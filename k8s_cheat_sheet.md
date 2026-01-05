## General

### create object with file
```bash
kubectl create -f flask_pod.yml
kubectl apply -f namespace.yml
```

### update object with file
```bash
kubectl apply -f flask_pod.yml
```

### delete object with file
```bash
kubectl delete -f flask_pod.yml
```


## Nodes

### show nodes
```bash
kubectl get nodes
```

### describe node
```bash
kubectl describe node docker-desktop
```

## Pods
### simple pod staring
```bash
kubectl run kuber-app-1 --image=flask_app --port=8000 --image-pull-policy=Never
```

### show pods
```bash
kubectl get pods
kubectl get pods --watch
```

### describe pod
```bash
kubectl describe pod kuber-app-1
```

### connect to pod
```bash
kubectl exec -it kuber-app-1 -- /bin/sh
kubectl exec -it kuber-app-1 --container kuber-app-1 -- /bin/sh
```

### forward ports <host_port:pod_port>
```bash
kubectl port-forward kuber-app-1 11000:8000
```

### show logs
```bash
kubectl logs kuber-app-1
kubectl logs kuber-app-1 --container kuber-app-1
```

### delete pod
```bash
kubectl delete pod kuber-app-1
```


## Labels

### show labels
```bash
kubectl get pods --show_labels
kubectl get pods -L app,db_type
```

### add label to pod
```bash
kubectl label pod flask-pod one_more_label=hello
```

### add label to node
```bash
kubectl label node docker-desktop first_node=true
```

### filter by labels
```bash
kubectl get pods -L app=flask_task_list
kubectl get pods -L app=flask_task_list,db_type=sqlite
kubectl get pods -L db_type!=postgres
kubectl get pods -l db_type     # has label
kubectl get pods -l '!db_type'  # has no label
kubectl get pods -l 'db_type in (sqlite, postgres)'
kubectl get pods -l 'db_type notin (sqlite, postgres)'
```

## Annotations
### add annotation to pod
```bash
kubectl annotate pod flask-pod description="simple task list app"
```

## Namespaces

### show namespaces
```bash
kubectl get ns
```

### create namespace
```bash
kubectl create namespace new-some-space
```

### create namespace
```bash
kubectl create namespace new-some-space
```

### delete namespace
```bash
kubectl delete namespace new-some-space
```


## Deployment

### show deployments
```bash
kubectl get deployment
kubectl get deployment some-dep -o yaml
```

### create deployment
```bash
kubectl create deployment some-dep --image=flask_app --port=8000 --replicas=3 --image-pull-policy=Never
kubectl apply -f deployment.yml --record
```

### change revision
```bash
kubectl set image deployment/some-dep flask-app-vlggb=hello_world --record
```

### show revision history
```bash
kubectl rollout history deployment some-dep
```

### rollback revision
```bash
kubectl rollout undo deployment some-dep
kubectl rollout undo deployment some-dep --to-revision=1
```

### delete deployment
```bash
kubectl delete deployment some-dep -n default
```

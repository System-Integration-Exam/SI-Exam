# SI-Exam

# How to run
### 1. Start minikube cluster
```
$ minikube start
```
### 2. Tunnel to cluster
_This blocks the terminal so run in seperate terminal window_
```
$ minikube tunnel
```
### 3. Apply kubernetes deployments
```
$ kubectl apply -R -f .kubernetes
```

### 4. Access to services
This can by default only be done through the gateway. If access to the service is needed, its possible to do a port forward in k8s by changing and running the command:
```
$ kubectl port-forward service/reservation-service 5000
```
# Playbooks Ansible Disponibles

## install_nginx.yml
Installation et configuration NGINX
- Install package nginx
- Configure virtual hosts
- Start service
- Setup firewall rules

## install_docker.yml  
Installation Docker CE
- Add Docker repository
- Install docker-ce
- Configure daemon
- Add user to docker group

## kubernetes_cluster.yml
Setup cluster Kubernetes
- Install kubeadm, kubelet, kubectl
- Initialize master node
- Join worker nodes
- Setup CNI networking

## monitoring_stack.yml
Deploy monitoring
- Install Prometheus
- Configure Grafana
- Setup alerting rules
- Deploy node exporters

## web_application.yml
Deploy web application
- Clone application code
- Install dependencies
- Configure database
- Setup reverse proxy

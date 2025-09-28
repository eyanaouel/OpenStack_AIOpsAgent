# Procédures de Déploiement

## Déploiement Serveur Web (NGINX)
1. Créer VM Ubuntu 22.04 avec flavor medium
2. Attendre activation complète (status ACTIVE)
3. Exécuter playbook install_nginx.yml
4. Configurer security group pour port 80/443
5. Tester connectivité HTTP
6. Configurer monitoring

## Déploiement Application Docker
1. Créer VM Ubuntu avec flavor large 
2. Exécuter playbook install_docker.yml
3. Configurer registry Docker privé
4. Déployer containers applicatifs
5. Setup load balancer si nécessaire

## Déploiement Cluster Kubernetes
1. Créer 3 VMs (1 master, 2 workers) flavor large
2. Exécuter playbook kubernetes_cluster.yml
3. Configurer CNI (Calico/Flannel)
4. Setup ingress controller
5. Déployer monitoring stack (Prometheus/Grafana)

## Résolution Problèmes Communs
- VM en ERROR: Vérifier quotas, redémarrer HARD
- Réseau inaccessible: Vérifier security groups et floating IPs
- Performance lente: Migrer vers compute node moins chargé
- Disk full: Étendre volumes ou nettoyer logs

## Playbooks Disponibles
- deploy_web_server.yml: Installation complète NGINX
- install_docker.yml: Installation Docker CE
- setup_kubernetes.yml: Cluster Kubernetes complet
- monitoring_stack.yml: Prometheus + Grafana

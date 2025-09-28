# Opérations Kubernetes

## Commandes Essentielles
kubectl get pods -A : Lister tous les pods
kubectl get nodes : État des nodes
kubectl get svc : Services exposés
kubectl logs <pod> : Logs d'un pod
kubectl describe pod <n> : Détails d'un pod

## Déploiements Standards
- Web app: deployment + service + ingress
- Base de données: statefulset + pvc + secret
- Cache: deployment + configmap + service

## Troubleshooting
- Pod en CrashLoopBackOff: Vérifier logs et ressources
- Service inaccessible: Vérifier selector et endpoints
- Node NotReady: Vérifier kubelet et réseau

## Actions Communes
- créer pod: kubectl run <name> --image=<image>
- exposer service: kubectl expose deployment <name> --port=80
- scaler: kubectl scale deployment <name> --replicas=3
- supprimer: kubectl delete <resource> <name>

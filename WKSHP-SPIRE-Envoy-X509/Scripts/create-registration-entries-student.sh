#/bin/bash

set -e

##bb=$(tput bold)
##nn=$(tput sgr0)

register() {
    kubectl exec -n spire spire-server-0 -c spire-server -- /opt/spire/bin/spire-server entry create $@
}

##echo "${bb}Creating registration entry for the backend - envoy...${nn}"
echo "Creating registration entry for the backend - envoy..."
register \
    -parentID spiffe://example.org/ns/spire/sa/spire-agent \
    -spiffeID spiffe://example.org/ns/testspiresds/sa/student{{ STDID }}/backend \
    -selector k8s:ns:testspiresds \
    -selector k8s:sa:student{{ STDID }} \
    -selector k8s:pod-label:app:backend-student{{ STDID }} \
    -selector k8s:container-name:envoy

##echo "${bb}Creating registration entry for the frontend - envoy...${nn}"
echo "Creating registration entry for the frontend - envoy..."
register \
    -parentID spiffe://example.org/ns/spire/sa/spire-agent \
    -spiffeID spiffe://example.org/ns/testspiresds/sa/student{{ STDID }}/frontend \
    -selector k8s:ns:testspiresds \
    -selector k8s:sa:student{{ STDID }} \
    -selector k8s:pod-label:app:frontend-student{{ STDID }} \
    -selector k8s:container-name:envoy

##echo "${bb}Creating registration entry for the frontend-2 - envoy...${nn}"
echo "Creating registration entry for the frontend-2 - envoy..."
register \
    -parentID spiffe://example.org/ns/spire/sa/spire-agent \
    -spiffeID spiffe://example.org/ns/testspiresds/sa/student{{ STDID }}/frontend-2 \
    -selector k8s:ns:testspiresds \
    -selector k8s:sa:student{{ STDID }} \
    -selector k8s:pod-label:app:frontend-2-student{{ STDID }} \
    -selector k8s:container-name:envoy

##echo "${bb}Listing created registration entries...${nn}"
##echo "Listing created registration entries..."
##kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry show

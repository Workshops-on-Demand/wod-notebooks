#/bin/bash

set -e

##bb=$(tput bold)
##nn=$(tput sgr0)


##echo "${bb}deleting registration entry for the backend - envoy...${nn}"
echo "deleting registration entry for the backend - envoy..."
BackendEntryID=$(kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry show | grep -B 1 -E 'spiffe.*testspiresds.*student{{ STDID }}.*backend' | grep 'Entry ID' | awk '{print $4}')
delBackendEntryID=$(echo $BackendEntryID | tr -d '\r')
echo $delBackendEntryID

kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry delete -entryID $delBackendEntryID

##echo "${bb}Deleting registration entry for the frontend-2 - envoy...${nn}"
echo "Deleting registration entry for the frontend-2 - envoy..."
Frontend2EntryID=$(kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry show | grep -B 1 -E 'spiffe.*testspiresds.*student{{ STDID }}.*frontend-2' | grep 'Entry ID' | awk '{print $4}') 
delFrontend2EntryID=$(echo $Frontend2EntryID | tr -d '\r')
echo $delFrontend2EntryID

kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry delete -entryID $delFrontend2EntryID

##echo "${bb}Deleting registration entry for the frontend - envoy...${nn}"
echo "Deleting registration entry for the frontend - envoy..."
FrontendEntryID=$(kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry show | grep -B 1 -E 'spiffe.*testspiresds.*student{{ STDID }}.*frontend' | grep 'Entry ID' | awk '{print $4}')
delFrontendEntryID=$(echo $FrontendEntryID | tr -d '\r')
echo $delFrontendEntryID

kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry delete -entryID $delFrontendEntryID

##echo "${bb}Listing created registration entries...${nn}"
###echo "Listing created registration entries..."
###kubectl exec -n spire spire-server-0 -- /opt/spire/bin/spire-server entry show

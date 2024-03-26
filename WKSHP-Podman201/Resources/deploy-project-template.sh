#!/bin/bash
oc create -f template.yaml -n openshift-config
cat << EOF |oc replace -f -
apiVersion: config.openshift.io/v1
kind: Project
metadata:
  name: cluster
spec:
  projectRequestTemplate:
    name: project-request
EOF
oc rollout restart deploy apiserver -n openshift-apiserver
watch oc get pod -n openshift-apiserver
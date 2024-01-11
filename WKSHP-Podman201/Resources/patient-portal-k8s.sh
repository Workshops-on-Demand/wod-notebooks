#!/bin/bash
oc new-project patient-portal-application
sleep 5
oc create deployment database --port 5432 --image quay.io/skupper/patient-portal-database -n patient-portal-application
oc set env deployment/database PGDATA=/var/lib/postgresql/data/patient-portal -n patient-portal-application
oc rollout restart deployment/database -n patient-portal-application
oc create deploy payment-processor --port 8080 --image quay.io/skupper/patient-portal-payment-processor -n patient-portal-application
sleep 5
oc create deployment frontend --image quay.io/skupper/patient-portal-frontend -n patient-portal-application
oc set env deployment/frontend -n patient-portal-application \
DATABASE_SERVICE_HOST="database" \
DATABASE_SERVICE_PORT="5432" \
PAYMENT_PROCESSOR_SERVICE_HOST="payment-processor" \
PAYMENT_PROCESSOR_SERVICE_PORT="8080"
oc expose deployment/database --port 5432 -n patient-portal-application
oc expose deployment/payment-processor --port 8080 -n patient-portal-application
oc expose deployment/frontend --port 8080 -n patient-portal-application
oc rollout restart deployment/frontend -n patient-portal-application
oc expose service/frontend -n patient-portal-application

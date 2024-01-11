#!/bin/bash
podman network create patient-portal-net
podman pod create --name patient-portal-pod --net patient-portal-net -p 8080:8080 #-p 5432:5432
podman run -d --rm --name database --pod patient-portal-pod quay.io/skupper/patient-portal-database
podman run -d --rm --name payment-processor --net patient-portal-net quay.io/skupper/patient-portal-payment-processor
sleep 10
podman run -d --rm --name frontend --pod patient-portal-pod \
-e DATABASE_SERVICE_HOST="localhost" \
-e DATABASE_SERVICE_PORT="5432" \
-e PAYMENT_PROCESSOR_SERVICE_HOST="payment-processor" \
-e PAYMENT_PROCESSOR_SERVICE_PORT="8080" \
quay.io/skupper/patient-portal-frontend
#!/bin/bash
podman network create database
podman network create payment
podman volume create patient-portal-data
podman run -d --rm --name database --network database -v patient-portal-data:/var/lib/postgresql/data quay.io/skupper/patient-portal-database
sleep 10
podman run -d --rm --name payment-processor --network payment quay.io/skupper/patient-portal-payment-processor
podman run -d --rm --name frontend --network payment,database -p 8080:8080 \
-e DATABASE_SERVICE_HOST="database" \
-e DATABASE_SERVICE_PORT="5432" \
-e PAYMENT_PROCESSOR_SERVICE_HOST="payment-processor" \
-e PAYMENT_PROCESSOR_SERVICE_PORT="8080" \
quay.io/skupper/patient-portal-frontend
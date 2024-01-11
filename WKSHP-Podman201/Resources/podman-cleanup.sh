#!/bin/bash
podman rm --all -f
podman network prune -f
podman volume prune -f
podman pod prune -f
podman image prune -f
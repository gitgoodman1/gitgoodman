# Apache Pulsar Pub/Sub Example with Python

This repository contains a sample project that demonstrates how to use **Apache Pulsar** for publishing and subscribing to messages using **Python**. The setup uses **Docker** to run Pulsar in standalone mode and **Python** scripts to create a publisher (sender) and a subscriber (receiver).

## Prerequisites

Make sure you have the following installed on your machine:

- [Python 3.x](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)

## Getting Started

### 1. Run Apache Pulsar in Docker

First, run Apache Pulsar standalone in Docker. This will start the Pulsar broker and admin service.

```bash
docker run -it -p 6650:6650 -p 8080:8080 \
  --name pulsar-standalone \
  apachepulsar/pulsar:latest \
  bin/pulsar standalone

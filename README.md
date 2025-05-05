# Zyrcle Backend - Sustainable Recycling Platform

The **Zyrcle Backend** powers the Zyrcle decentralized application (dApp), enabling sustainable recycling by integrating IoT smart containers, AI-driven route optimization, and data management for a blockchain-based recycling platform on **Avalanche**. Built with **Python**, this backend handles container scanning, residence stats, collector routes, and IoT data processing, supporting the React and Web3.js frontend.

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Key Services and Routes](#key-services-and-routes)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Zyrcle Backend provides APIs and services to manage recycling operations, including IoT container data, residence dashboards, collector routes, and statistics. It integrates with IoT sensors for real-time container data, uses AI (via Gemini API) for route optimization, and stores container metadata in `containers.json`. The backend supports the frontend by providing data for wallet-based container access, token rewards, and carbon credit NFT minting on Avalanche.

## Directory Structure
zyrcle-backend/
├── models/
│   ├── iot.py               # IoT container data models
│   ├── route.py            # Route models for collectors
│   └── stats.py            # Stats models for recycling metrics
├── routes/
│   ├── iot.py              # Endpoints for IoT container data
│   ├── residencia.py       # Endpoints for residence dashboards
│   ├── rutas.py            # Endpoints for collector routes
│   ├── scan.py             # Endpoints for container scanning
│   ├── stats.py            # Endpoints for recycling statistics
│   └── status.py           # Endpoints for system status
├── services/
│   ├── gemini.py           # Gemini API integration for AI features
│   ├── iot_service.py      # Logic for IoT container data processing
│   ├── residence_service.py # Logic for residence-related data
│   ├── scan_containers.py  # Logic for container scanning (e.g., QR codes)
│   └── stats_service.py    # Logic for calculating stats and CO₂ savings
├── containers.json         # Static container data (e.g., locations, types)
├── main.py                 # Entry point for the backend
├── README.md               # This file
└── requirements.txt        # Python dependencies

## Key Services and Routes

### Services

- **`gemini.py`**: Integrates Google’s Gemini API for AI-driven features, such as optimizing collection routes for collectors based on container fill levels.
- **`iot_service.py`**: Processes IoT sensor data (e.g., fill level, weight) from smart containers and updates `containers.json`.
- **`residence_service.py`**: Manages residence data, including total containers, weight, and CO₂ savings for dashboards.
- **`scan_containers.py`**: Handles container access via QR codes or 6-digit codes, verifying user access against wallet addresses (via frontend Web3.js).
- **`stats_service.py`**: Calculates recycling stats, such as total weight, tokens earned, and CO₂ saved, for display on dashboards.

### Routes

- **`iot.py`**: Endpoints to fetch IoT container data (e.g., `/api/iot/containers/{id}` for fill level, weight).
- **`residencia.py`**: Endpoints for residence dashboards (e.g., `/api/residence/stats` for metrics like total weight, CO₂ saved).
- **`rutas.py`**: Endpoints for collector routes (e.g., `/api/routes/optimize` to generate optimized routes using Gemini AI).
- **`scan.py`**: Endpoints for container scanning (e.g., `/api/scan/{code}` to validate QR codes or manual codes).
- **`stats.py`**: Endpoints for stats (e.g., `/api/stats/monthly` for material breakdown, CO₂ savings).
- **`status.py`**: Endpoints for system health (e.g., `/api/status` to check backend availability).


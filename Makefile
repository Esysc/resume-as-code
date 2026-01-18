# Makefile for CV as Code

.PHONY: help install dev build test clean generate

help:
	@echo "CV as Code - Development Tasks"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help      Show this help message"
	@echo "  install   Install all dependencies"
	@echo "  generate  Generate CV outputs (HTML/JSON/PDF)"
	@echo "  dev       Start development server"
	@echo "  build     Build production app"
	@echo "  test      Run tests"
	@echo "  clean     Remove generated files"
	@echo "  lint      Lint code"

install:
	pip install -r backend/requirements.txt
	pip install -U pylint
	cd web && npm install

generate:
	python backend/generate.py

dev:
	cd web && npm run dev

build:
	python backend/generate.py
	cd web && npm run build

test:
	pytest tests/ -v

clean:
	rm -rf dist/
	rm -rf web/dist
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	python -m pylint backend/**/*.py
	cd web && npm run lint

.DEFAULT_GOAL := help

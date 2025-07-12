"""
Configuração do pytest para o projeto HireMe.
"""
import pytest
import sys
import os

# Adiciona o diretório raiz do projeto ao path para importações
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
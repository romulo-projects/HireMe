import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock
from HireMe.gui import setup_ui


@pytest.mark.skipif(not hasattr(tk, 'Tk'), reason="No display available")
def test_setup_ui_creates_window():
    """Testa se a função setup_ui cria uma janela tkinter."""
    try:
        app = setup_ui()
        
        # Verifica se retorna uma instância de Tk
        assert isinstance(app, tk.Tk)
        
        # Verifica se o título foi definido
        assert app.title() == "HireMe - Automatizador de Currículos"
        
        # Verifica se a geometria foi definida
        assert "400x200" in app.geometry()
        
        # Fecha a janela para evitar problemas
        app.destroy()
    except tk.TclError:
        pytest.skip("No display available for GUI testing")


@patch('HireMe.gui.analyze_resume')
@patch('HireMe.gui.generate_pdf_resume')
@patch('tkinter.filedialog.askopenfilename')
@patch('tkinter.filedialog.asksaveasfilename')
@patch('tkinter.messagebox.showinfo')
def test_gui_imports_work(mock_showinfo, mock_saveas, mock_open, mock_generate, mock_analyze):
    """Testa se todas as importações necessárias funcionam."""
    # Importa as funções para verificar se não há erros de importação
    from HireMe.gui import select_resume_file, process_resume, setup_ui
    
    # Verifica se as funções existem
    assert callable(select_resume_file)
    assert callable(process_resume)
    assert callable(setup_ui)


def test_gui_module_structure():
    """Testa a estrutura básica do módulo GUI."""
    import HireMe.gui as gui_module
    
    # Verifica se as funções principais existem
    assert hasattr(gui_module, 'setup_ui')
    assert hasattr(gui_module, 'select_resume_file')
    assert hasattr(gui_module, 'process_resume')
    
    # Verifica se são callable
    assert callable(gui_module.setup_ui)
    assert callable(gui_module.select_resume_file)
    assert callable(gui_module.process_resume)
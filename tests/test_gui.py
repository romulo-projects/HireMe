import pytest
import tempfile
import os
from unittest.mock import patch, MagicMock


def test_gui_module_imports():
    """
    Testa se o módulo GUI pode ser importado corretamente.
    """
    try:
        import HireMe.gui
        assert hasattr(HireMe.gui, 'setup_ui')
        assert hasattr(HireMe.gui, 'select_resume_file')
        assert hasattr(HireMe.gui, 'process_resume')
    except ImportError:
        pytest.fail("Falha ao importar o módulo GUI")


@patch.dict('os.environ', {'DISPLAY': ':0'})
@patch('tkinter.Tk')
def test_setup_ui_basic(mock_tk):
    """
    Testa se a função setup_ui pode ser chamada.
    """
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    
    # Mock StringVar para evitar problemas de tkinter
    with patch('tkinter.StringVar') as mock_stringvar:
        mock_stringvar.return_value = MagicMock()
        
        from HireMe.gui import setup_ui
        result = setup_ui()
        
        assert result == mock_root
        mock_tk.assert_called_once()


def test_gui_functions_exist():
    """
    Testa se as principais funções da GUI existem.
    """
    from HireMe import gui
    
    # Verifica se as funções principais existem
    assert callable(getattr(gui, 'setup_ui', None))
    assert callable(getattr(gui, 'select_resume_file', None))
    assert callable(getattr(gui, 'process_resume', None))
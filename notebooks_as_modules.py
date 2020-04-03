from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec
from importlib.util import spec_from_loader
from IPython import get_ipython
from nbformat.reader import read as read_notebook
import os
import os.path as op
import sys
from types import ModuleType
from typing import *


def notebook_for_module(name_module: str):
    return f"{name_module}.ipynb"


class NotebookImporter(MetaPathFinder, Loader):
    """
    Enables the importation of notebooks in the current directory as modules.
    """

    def find_spec(self, name_full: str, path: os.PathLike, target) -> Optional[ModuleSpec]:
        name_notebook = notebook_for_module(name_full)
        if os.access(name_notebook, os.R_OK):
            return spec_from_loader(name_full, self, origin=op.realpath(name_notebook))
        return None

    def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
        return None

    def exec_module(self, module: ModuleType) -> None:
        # TBD: leverage internal anchors to provide in-notebook code locations.
        name_notebook = notebook_for_module(module.__name__)
        with open(name_notebook, "rb") as file_notebook:
            notebook = read_notebook(file_notebook)
        for num_cell, cell in enumerate([c for c in notebook.cells if c.cell_type == "code"], 1):
            if not cell.source.strip().startswith("%") and "noimport" not in cell.metadata.get("tags", []):
                name_cell = f"{name_notebook} Cell {num_cell}"
                ipython = get_ipython()
                if ipython:
                    name_cell = ipython.compile.cache(cell.source)
                code = compile(cell.source, name_cell, "exec")
                exec(code, module.__dict__)


sys.meta_path.append(NotebookImporter())

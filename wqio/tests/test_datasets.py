import os
import tempfile
import shutil

import pytest
from pandas.util.testing import network

from wqio import datasets


@network(url='https://github.com/Geosyntec/water-quality-dataset')
@pytest.mark.parametrize('fname', ['bmpdata', 'nsqd'])
def test_download(fname):
    with tempfile.TemporaryDirectory() as tmpdir:
        fname = datasets.download(fname, data_dir=tmpdir)
        assert os.path.exists(fname)

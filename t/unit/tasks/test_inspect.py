import inspect
import pytest

class test_DjangoWorkerFixup():
    @pytest.mark.patched_module('django', 'django.core')
    def test_validate_models(self, patching, module):
        # the following line and the module fixture are both necessary for the bug
        patching.modules('django.core.checks')
        # effectively this is the same as:
        # patching.modules('django', 'django.core', 'django.core.checks')

        # so conftext._module is first called with names=('django', 'django.core')
        # then with names=('django', 'django.core', 'django.core.checks')

        # conftest.py:L545
        # Breakpoint in the finally block first hit with names=('django', 'django.core'), prev={}
        # then with names=('django', 'django.core', 'django.core.checks'), prev={'django': <MockModule>, 'django.core': <MockModule>}
        # but the finalizer registered by patching.modules runs first



class test_ZZZ:
    def test_inspect(self):
        inspect.stack()

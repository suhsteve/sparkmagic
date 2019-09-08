# Copyright (c) 2015  aggftw@gmail.com
# Distributed under the terms of the Modified BSD License.
from sparkmagic.utils.constants import LANG_CSHARP
from sparkmagic.kernels.wrapperkernel.sparkkernelbase import SparkKernelBase


class SparkDotnetKernel(SparkKernelBase):
    def __init__(self, **kwargs):
        implementation = 'Spark .NET'
        implementation_version = '1.0'
        language = 'no-op'
        language_version = '0.1'
        language_info = {
            'name': 'sparkdotnet',
            'mimetype': 'text/x-csharp',
            'codemirror_mode': 'text/x-csharp',
            'pygments_lexer': 'csharp'
        }

        session_language = LANG_CSHARP

        super(SparkDotnetKernel, self).__init__(implementation, implementation_version, language, language_version,
                                            language_info, session_language, **kwargs)


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=SparkDotnetKernel)

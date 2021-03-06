from distutils.core import setup

setup(
    name='fasterpay',
    version='0.1.0',
    author='FasterPay Integration Team',
    author_email='integration@paymentwall.com',
    packages=['fasterpay', 'fasterpay.tests', 'fasterpay.validator', 'fasterpay.request'],
    url='http://pypi.python.org/pypi/FasterPay/',
    license='LICENSE',
    description='FasterPay Python Integration SDK',
    long_description=open('README.md').read(),
)

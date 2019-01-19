from setuptools import setup, find_packages

setup(
	name='honest',
	description='Honest Rest API',
	version='0.0.1-dev',
	install_requires=(
		'requests',
		'Flask',
		'pymongo',
	),
	packages=find_packages(),
	license='MIT',
	zip_safe=False,
	test_suite='nose.collector',
    tests_require=['nose'],
)

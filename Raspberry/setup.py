try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup


config = [
        'description': 'Pedestrian detection with web communication',
        'author': 'Artur Nowak',
        'author email': 'artur.marek.nowak@gmail.com',
        'version': '0.1'
        'install requires': ['OpenCV', 'imutils', 'numpy'],
        'packages': ['Detection'],
        'scripts': [],
        'name': 'Pedestrian detection'
]

setup(**config)

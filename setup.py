from distutils.core import setup

setup(
    name='community_detect',
    version='1.0.0_1',
    packages=['community_detect'],
    url='https://github.com/javipalanca/community-detect',
    license='Apache License 2.0',
    install_requires=["networkx", "matplotlib"],
    author='Ankush Bhatia',
    author_email='ankushbhatia02@gmail.com',
    description='Community Detector based on algorithm for community detection using structural and attribute similarities'
)

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='v_vk_api',
      packages=['v_vk_api'],
      description='VK API wrapper',
      long_description=readme,
      version='1.1',
      url='https://github.com/vadimk2016/v-vk-api',
      author='Vadim Kuznetsov',
      author_email='vadim.kuznyetsov@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3',
          'Topic :: Internet'
      ],
      keywords='v-vk-api',
      python_requires='>=3',
      install_requires=[
          'beautifulsoup4==4.6.0',
          'certifi==2018.4.16',
          'chardet==3.0.4',
          'idna==2.6',
          'requests==2.18.4',
          'urllib3==1.22'
      ],
      )

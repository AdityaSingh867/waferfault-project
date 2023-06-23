from setuptools import setup , find_packages

setup(
    name="src",
    version='0.0.5',
    author='Aditya Singh',
    author_email="uniquesingh@gmail.com",
    packages=find_packages(),
    install_requires=['database-connect','aiofiles','dill','dnspython','evidently'
                      ,'Flask','httptools','imblearn','jinja2','mypy-boto3-s3',
                      'pip-chill','pymongo','python-dotenv','python-multipart',
                      'seaborn','types-s3transfer','uvicorn','watchfiles',
                      'websockets','wincertstore','xgboost','neuro-mf','boto3','scikit-learn'])

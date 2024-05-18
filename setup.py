# setup.py
import subprocess
import sys

def install_packages():
    packages = [
        'pandas', 'numpy', 'faker', 'matplotlib', 'seaborn', 'nltk', 
        'textblob', 'scikit-learn', 'wordcloud'
    ]
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()

    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

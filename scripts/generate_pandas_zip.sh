cd ..
root_dir=$(pwd)
tmp_dir=$root_dir/.tmp
mkdir -p $tmp_dir

cd $tmp_dir
mkdir -p pandas_layer/python
cd ./pandas_layer/python
curl -s -o numpy.whl https://files.pythonhosted.org/packages/f4/f4/45e6e3f7a23b9023554903a122c95585e9787f9403d386bafb7a95d24c9b/numpy-1.24.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
curl -s -o pandas.whl https://files.pythonhosted.org/packages/e1/4d/3eb96e53a9208350ee21615f850c4be9a246d32bf1d34cd36682cb58c3b7/pandas-1.5.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
curl -s -o pytz.whl https://files.pythonhosted.org/packages/2e/09/fbd3c46dce130958ee8e0090f910f1fe39e502cc5ba0aadca1e8a2b932e5/pytz-2022.7.1-py2.py3-none-any.whl
unzip -qq -o numpy.whl -d .
unzip -qq -o pandas.whl -d .
unzip -qq -o pytz.whl -d .
rm *.whl
cd ../
zip -qq -r ../pandas_layer.zip ./python
cd ../
rm -r ./pandas_layer

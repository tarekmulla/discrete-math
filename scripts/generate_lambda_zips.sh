cd ..
root_dir=$(pwd)
infra_dir=$root_dir/infrastructure
tmp_dir=$root_dir/.tmp
mkdir -p $tmp_dir

cd $infra_dir/modules/lambda_layers/utility
zip -qq -r $tmp_dir/utility_layer.zip ./python
cd $infra_dir/modules/api/cors/src/
zip -qq -r -j $tmp_dir/cors.zip .
cd $infra_dir/modules/api/generate_question/src/
zip -qq -r -j $tmp_dir/generate_question.zip .

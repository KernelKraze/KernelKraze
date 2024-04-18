npm run build
sleep 1
rm ../assets ../favo.svg ../index.html -rf 
mv ./dist/* ../
rm ./dist/ -rf

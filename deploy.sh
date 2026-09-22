chars='abcdef0123456789'
length=32
result=""
for ((i=0; i<length; i++)); do
    result+="${chars:RANDOM%${#chars}:1}"
done
echo "$result"
echo "DEBUG = False \n SECRET_KEY=$result" > ./cat_api/.env
git add .
git commit -m "$1"
git push origin master
render deploys create srv-dajm90h594qs73coloq0 --confirm --wait
echo "DEBUG = False \n SECRET_KEY=$result" > ./cat_api/.env

chars='abcdef0123456789'
length=16
result=""
for ((i=0; i<length; i++)); do
    result+="${chars:RANDOM%${#chars}:1}"
done
echo "$result"

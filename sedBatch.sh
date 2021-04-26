while read line; do 
    sed -i 's/regsnp-django-app/regsnp-django-app/g' $line
done < out.txt

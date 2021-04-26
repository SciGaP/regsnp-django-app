while read line; do 
    sed -i 's/regsnp-django-app/regsnp_django_app/g' $line
done < out.txt

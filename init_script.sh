#!/bin/bash
set -o nounset
set -o errexit

declare -a names=("Peter" "Damon" "Kurt" "Agapetos" "Marinette" "Monroe"
                  "Gerard" "Purnima" "Yuri" "Doncho" "Joe")
declare -a moves=("Sunder" "Kick" "Hex" "Wreck" "Ambush" "Strike" "Fever"
                  "Devotion" "Sidestep" "Enthrall", "Snare")
host_name='http://localhost:8000'


docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

m=0
for n in "${names[@]}"
do
    move=${moves[$m]}
    exp=$(( ( RANDOM % 10 ) + 1 ))
    curl --request POST \
         --header "Content-Type: application/json" \
         --data-binary '{
                "name": "'$n'",
                "powermove": "'$move'",
                "experience": '$exp',
                "out_of_order": false,
                "avatar": "https://robohash.org/'$n'.png"
          }' \
    $host_name'/robots/' -k

    let m=$m+1
done

for i in {1..10}
do
    let s=$i+1
    for j in $(seq $s 10)
    do
        curl --request POST \
             --header "Content-Type: application/json" \
             --data-binary '{
                "r1": '$i',
                "r2": '$j',
                "winner": '$i'
                }' \
        $host_name'/battles/' -k

        curl --request POST \
             --header "Content-Type: application/json" \
             --data-binary '{
                "r1": '$i',
                "r2": '$j',
                "winner": '$j'
                }' \
        $host_name'/battles/' -k

    done
done


curl --request POST \
     --header "Content-Type: application/json" \
     --data-binary '{
        "battles": [1, 35, 61, 79, 89]
        }' \
$host_name'/danceoffs/' -k

curl --request POST \
     --header "Content-Type: application/json" \
     --data-binary '{
        "battles": [19, 49, 71, 85, 17]
        }' \
$host_name'/danceoffs/' -k
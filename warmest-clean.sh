for i in raw/*; do echo $i; jq -r '[.items[].recording | {name: .title, artists: [.artists[].name]}]' $i > clean/$(basename $i); done

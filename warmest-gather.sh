start='2015-01-22T01:00:00'
end='2016-01-22T01:00:00'

# Loop from start to end date
while [[ $(date -d $start +"%s") -lt $(date -d $end +"%s") ]]; do
    echo $start >&2
    # The URL and output filename
    url="http://music.abcradio.net.au/api/v1/plays/search.json?station=triplej&from=$start&order=asc"
    output_fn="raw/$start"
    # Download the list
    curl $url > $output_fn
    # Get the time of the last song played
    start=$(jq -r '.items[].played_time' $output_fn |tail -n1)
    # Add one second so it doesn't include the last song next time
    start=$(date -u -d "$start + 1 second" +"%Y-%m-%dT%H:%M:%S")
done

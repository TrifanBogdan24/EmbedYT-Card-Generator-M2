#!/bin/bash


rm -rf URLs/ out/
mkdir URLs/ out/



iter=0

# Read the file line by line
while IFS= read -r url ; do
    iter=$(($iter+1))
    echo "$url" > "URLs/$iter.txt"
    
    # Give it more try. Pytube is not quite responsive. Might be prone to errors
    for i in $(seq 1 10) ; do
        python3 ../html_md_youtube_card.py "$url" 2> /dev/null 1> "ref/$iter.md"
        if [[ $? == 0 ]] ; then
            # If the script did not return an error code, exit the for
            break
        fi
    done
done < URLs.txt




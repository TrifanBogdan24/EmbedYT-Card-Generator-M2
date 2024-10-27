#!/bin/bash


rm -rf out/
mkdir out/

exit_code=0
iter=0

echo '' > err.txt

# Read the file line by line
while IFS= read -r url ; do
    iter=$(($iter+1))
    
    echo "$url" > "URLs/$iter.txt"
    echo -n "Testing URL $iter: "

    script_exit_code=0


    # Give it more try. Pytube is not quite responsive. Might be prone to errors
    for i in $(seq 1 10) ; do

        python3 ../html_yt_card.py "$url" 2> err.txt 1> "out/$iter.md"
        
        script_exit_code=$?


        if [[ $script_exit_code == 0 ]] ; then
            
            nr_diff_lines=$(diff out/$iter.md ref/$iter.md | wc -l)

            if [[ $nr_diff_lines != 0 ]] ; then
                exit_code=255
                echo "[ERROR] For URLs/$iter.txt, the following command doesn't OUTPUT as expected:"
                echo "$ python3 ../html_yt_card.py " "$url"
                diff "out/$iter.md" "ref/$iter.md"
                echo ''
                break
            else
                echo "[OK] URLs/$iter.txt"
                break
            fi
            
            # If the script did not return an error code, exit the for
            break
        fi
    done

    if [[ $script_exit_code != 0 ]] ; then
        exit_code=255
        echo "[ERROR] For URLs/$iter.txt, the following command produces an ERROR message"
        echo "$ python3 ../html_yt_card.py " "$url"
        echo "Error message:"
        cat err.txt
        echo ''
    fi

done < URLs.txt


echo ''
rm -rf err.txt

if [[ $exit_code == 0 ]] ; then
    echo "Great! All tests PASSED"
else
    echo "Some tests FAILED :(("
fi

exit $exit_code

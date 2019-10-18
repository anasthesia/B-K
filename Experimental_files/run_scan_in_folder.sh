#run ./script.sh inputfolder BR
for f in "$1"/*.dat; do
    python parameter_scan.py "$f" "$2"
done
